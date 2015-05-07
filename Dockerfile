# Copyright 2014 Alien Laboratories, Inc.


# TODO(burdon): Write up GUIDES (self contained docs).
# TODO(burdon): Get rid of pydeps
# TODO(burdon): Use vagrant to test locally?

# HOW TO TEST APP IS RUNNING? TRY SIMPLE TUTORIAL (might have paths wrong?)
# LOGS?
# ssh into container?


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
# curl $(boot2docker ip):5000
# nc -v $(boot2docker ip) 5000
# docker stop dev
# docker ps

# docker logs -f dev


# Base python image (includes tools)
# https://registry.hub.docker.com/u/library/python/
FROM python:2.7.9

# File Author
MAINTAINER Alien Labs

# Install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

# Bundle app source
ADD src/main/python /src

# Expose (default Flask port)
EXPOSE 5000

# TODO(burdon): nginx
# Run the server
CMD ["python", "/src/main.py"]
