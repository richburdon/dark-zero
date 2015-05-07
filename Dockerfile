# Notes
# http://www.fullstackpython.com/docker.html
# http://blogs.aws.amazon.com/application-management/post/Tx1ZLAHMVBEDCOC/Dockerizing-a-Python-Web-App
# https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications

# https://registry.hub.docker.com/u/library/python/


# Test locally
# tools/python/bin/python src/main/python/main.py
# curl localhost:5000

# boot2docker init
# boot2docker start
# boot2docker status
# $(boot2docker shellinit)

# docker ps
# docker rm -f ID

# https://github.com/dockerfile/nginx/blob/master/Dockerfile
# docker run -d -P --name web nginx

# docker build -t app .                   TAG = "app"
# docker run -d -P --name dev app         CONTAINER = "dev"
# docker ps
# docker port dev
# curl $(boot2docker ip):5000
# nc -v $(boot2docker ip) 5000
# docker stop dev
# docker ps

# docker logs -f dev


# HOW TO TEST APP IS RUNNING?
# LOGS?


# Base image
# https://registry.hub.docker.com/u/library/python/
FROM python:2.7.9

# File Author
MAINTAINER Alien Labs

# Install Python modules
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

# Bundle app source
ADD src/main/python /src

# Expose
EXPOSE 5000

# Run the server
CMD ["python", "/src/main.py"]
