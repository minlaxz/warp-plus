# warp-plus-gui
# Author: deathlyface
# Modified from: ALIILAPRO/warp-plus-cloudflare

from flask import Flask, request, render_template, jsonify
from datetime import datetime
from config import *
import urllib.request, json, string, random

app = Flask(__name__)

print("Running warp-plus-gui with proxy={}, custom_proxy={}, max_retry={}".format(proxy_enabled, False if len(custom_proxy) == 0 else True, max_retry))

def randomString(length):
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(length))

def randomDigit(length):
	digit = string.digits
	return ''.join((random.choice(digit) for i in range(length)))

def getData(uid):
	url = f'https://api.cloudflareclient.com/v0a{randomDigit(3)}/reg'
	install_id = randomString(22)
	body = {
		"key": "{}=".format(randomString(43)),
		"install_id": install_id,
		"fcm_token": "{}:APA91b{}".format(install_id, randomString(134)),
		"referrer": uid,
		"warp_enabled": False,
		"tos": datetime.now().isoformat()[:-3] + "+02:00",
		"type": "Android",
		"locale": "es_ES"
	}
	data = json.dumps(body).encode('utf8')
	headers = {
		'Content-Type': 'application/json; charset=UTF-8',
		'Host': 'api.cloudflareclient.com',
		'Connection': 'Keep-Alive',
		'Accept-Encoding': 'gzip',
		'User-Agent': 'okhttp/3.12.1'
	}
	req = urllib.request.Request(url, data, headers)
	if proxy_enabled:
		if len(custom_proxy) == 0:
			try:
				with urllib.request.urlopen('https://api.getproxylist.com/proxy?protocol[]=http&minDownloadSpeed=400&anonymity[]=high%20anonymity&allowsCustomHeaders=1&allowsPost=1&allowsHttps=1&maxSecondsToFirstByte=1') as response:
					proxy = json.loads(response.read())
					req.set_proxy("{}:{}".format(proxy["ip"], proxy["port"]), proxy["protocol"])
			except:
				print("Failed to set proxy from getproxylist.com.")
		else:
			try:
				req.set_proxy(custom_proxy["host"], custom_proxy["protocol"])
			except:
				print("Failed to set custom proxy.")
	try:
		response = urllib.request.urlopen(req)
		status_code = response.getcode()
		return True if status_code == 200 else False
	except Exception as e:
		print(e)
		return False

@app.route("/")
def root():
    return render_template("index.html", proxy=proxy_enabled, host=request.host_url)

@app.route("/get")
def get():
	referrer = request.args["uid"]
	if referrer is None:
		return render_template("index.html", host=request.host_url, proxy=proxy_enabled, color="red", success=str(datetime.utcnow())[:-7] + " UTC: Failed to add 1GB Warp+ data.")
	for x in range(max_retry):
		success = getData(referrer)
		if success:
			return render_template("index.html", host=request.host_url, proxy=proxy_enabled, color="green", success=str(datetime.utcnow())[:-7] + " UTC: Successfully added 1GB Warp+ data.")

	return render_template("index.html", host=request.host_url, proxy=proxy_enabled, color="red", success=str(datetime.utcnow())[:-7] + " UTC: Failed to add 1GB Warp+ data.")

@app.route("/getjson")
def getjson():
	referrer = request.args["uid"]
	for x in range(max_retry):
		success = getData(referrer)
		if success:
			return jsonify({"success": success, "proxy": proxy_enabled})

	return jsonify({"success": success, "proxy": proxy_enabled})