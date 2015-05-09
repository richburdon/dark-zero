#!/bin/sh

echo "### Exporting boot2docker env"
boot2docker status
$(boot2docker shellinit)
echo ""

# TODO(burdon): Move to Gruntfile/Fleet.
echo "### Cleaning up"
docker ps
docker rm -f web
docker rm -f graphdb
echo ""

# https://github.com/kbastani/docker-neo4j
echo "### Starting graphdb"
docker pull kbastani/docker-neo4j
docker run -d -p 7474:7474 -v /home/docker/neo4j/data:/opt/data --name graphdb kbastani/docker-neo4j
echo ""

# Allow access from $(boot2docker ip):7474/browser
# sudo route add -net 172.17.0.0/16 $(boot2docker ip 2> /dev/null)

# Build a local image (from Dockerfile) and run it.
echo "### Starting web"
docker build -t app .
# Link database
# https://docs.docker.com/userguide/dockerlinks
docker run -d -p 8080 --name web --link graphdb:graphdb app
echo ""

# Test
echo "### Testing"
docker ps
PORT=$(docker port web | cut -d ':' -f 2)
echo $(boot2docker ip):${PORT}
curl $(boot2docker ip):${PORT}
curl $(boot2docker ip):${PORT}/data
echo ""
