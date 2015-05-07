#!/bin/sh

# TODO(burdon): Move to Gruntfile.
docker ps
docker rm -f dev

# Build a local image (from Dockerfile) and run it.
docker build -t app .
docker run -d -p 80 --name dev app

docker ps
boot2docker ip
docker port dev

# Test
curl $(boot2docker ip):$(docker port dev | cut -d ':' -f 2)
echo ""
