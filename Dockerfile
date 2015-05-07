# Copyright 2014 Alien Laboratories, Inc.

# http://viget.com/extend/how-to-use-docker-on-os-x-the-missing-guide
# https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications

# TODO(burdon): Write up GUIDES (self contained docs).
# TODO(burdon): Get rid of pydeps
# TODO(burdon): Use vagrant to test locally?

# HOW TO TEST APP IS RUNNING? TRY SIMPLE TUTORIAL (might have paths wrong?)
# LOGS?
# ssh into container?

# TODO(burdon): Grunt/docker

# Test locally
# tools/python/bin/python src/main/python/main.py
# curl localhost:5000

# Local docker environment (via VirtualBox)
# "docker" CLI communicates with a daemon; on OS/X this is provided by boot2docker
# docker connected to the daemon via the DOCKER_HOST environment variable
# boot2docker init
# boot2docker start
# boot2docker status
# $(boot2docker shellinit)
# boot2docker ip

# List running containers
# docker ps
# docker stop ID
# docker rm -f ID

# Run a standard image
# https://github.com/dockerfile/nginx/blob/master/Dockerfile
# docker run -d -P --name web nginx

# Build a local image (from Dockerfile) and run it
# docker build -t app .                   TAG = "app"
# docker run -d -P --name dev app         CONTAINER = "dev"
# docker ps
# docker port dev
# curl $(boot2docker ip):80
# nc -v $(boot2docker ip) 80
# docker stop dev
# docker ps

# docker inspect dev
# docker logs -f dev

# Base python image (includes tools)
# https://registry.hub.docker.com/_/python/
# https://registry.hub.docker.com/u/library/python/
# https://github.com/docker-library/python/blob/master/2.7/Dockerfile
FROM python:2.7.9

# File Author
MAINTAINER Alien Labs

# Base dir
WORKDIR /app

# TODO(burdon): limit source?
ADD . /app

# Install Python modules
RUN pip install -r requirements.txt

# Expose (default Flask port)
EXPOSE 80

# TODO(burdon): nginx
# Run the server
CMD ["python", "src/main/python/hello.py"]
