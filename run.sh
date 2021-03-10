docker build -t warp . && \
docker run --name warp -d -p 8000:5000 \
--volume $PWD:/app
--restart unless-stopped \
--memory='512m' --cpus=0.5 \
warp:latest