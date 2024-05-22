## docker of melotts

### build docker
```shell
docker build . -t samge/melotts -f .devcontainer/release/Dockerfile-release --build-arg PROXY=http://192.168.50.48:7890
```

### upload
```shell
docker push samge/melotts
```

### run
```shell
docker run -itd \
--name melotts \
-v /path/to/your/host/volume:/root/.cache \
-e NVIDIA_VISIBLE_DEVICES=1 \
--gpus all \
--shm-size 22g \
-p 18188:8000 \
-p 17860:7860 \
--restart unless-stopped \
samge/melotts
```