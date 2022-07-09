docker build -t warp . && \
docker run --name warpper -d -p 6969:5000 \
--volume $PWD:/app
--restart unless-stopped \
--memory='512m' --cpus=0.5 \
warp:latest