# Copyright 2014 Alien Laboratories, Inc.

# http://viget.com/extend/how-to-use-docker-on-os-x-the-missing-guide
# https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications

# TODO(burdon): Write up GUIDES (self contained docs).
# TODO(burdon): Grunt/docker
# TODO(burdon): Get rid of pydeps?

# TODO(burdon): Slim?
# Base python image (includes tools)
# https://registry.hub.docker.com/_/python/
# https://registry.hub.docker.com/u/library/python/
# https://github.com/docker-library/python/blob/master/2.7/Dockerfile
FROM python:2.7.9

# File Author
MAINTAINER Alien Labs

# TODO(burdon): restrict source?
ADD . /app

# Base dir for build
WORKDIR /app

# Install Python modules
RUN pip install -r requirements.txt

# Expose (default Flask port)
# NOTE: Port 80 requires sudo
EXPOSE 8080

# Base dir for server
WORKDIR /app/src/main/python

# Run the server
CMD ["python", "main.py"]
