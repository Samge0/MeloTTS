## docker of melotts-dev

### build docker
```shell
docker build . -t samge/melotts-dev-base -f .devcontainer/Dockerfile-dev-base --build-arg PROXY=http://192.168.50.48:7890
```

### upload
```shell
docker push samge/melotts-dev-base
```

### run .devcontainer/devcontainer.json