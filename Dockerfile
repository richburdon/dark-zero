# Copyright 2014 Alien Laboratories, Inc.

# http://viget.com/extend/how-to-use-docker-on-os-x-the-missing-guide
# https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications

# TODO(burdon): Write up GUIDES (self contained docs).
# TODO(burdon): Grunt/docker
# TODO(burdon): Get rid of pydeps
# TODO(burdon): Use vagrant to test locally?

# Base python image (includes tools)
# https://registry.hub.docker.com/_/python/
# https://registry.hub.docker.com/u/library/python/
# https://github.com/docker-library/python/blob/master/2.7/Dockerfile
FROM python:2.7.9

# File Author
MAINTAINER Alien Labs

# Base dir
WORKDIR /app

# TODO(burdon): restrict source?
ADD . /app

# Install Python modules
RUN pip install -r requirements.txt

# Expose (default Flask port)
EXPOSE 8080

# TODO(burdon): nginx
# Run the server
#CMD ["python", "src/main/python/hello.py"]
CMD ["python", "src/main/python/main.py"]
