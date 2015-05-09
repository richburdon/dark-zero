#!/bin/sh
# ssh root@45.55.200.124 'bash -s' < deploy_prod.sh

export FLASK_ENV=PRODUCTION

docker rm -f graphdb
docker rm -f web

docker pull kbastani/docker-neo4j
docker run -d -p 7474:7474 -v /home/docker/neo4j/data:/opt/data --name graphdb kbastani/docker-neo4j

docker pull richburdon/dark-zero
docker run -d -p 80:8080 --link graphdb:graphdb --name web richburdon/dark-zero

docker ps
