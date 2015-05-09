#!/bin/sh

# TODO(burdon): Work in progress for deploy script.
# https://circleci.com/docs/docker

NAME=dark-zero

# Exit on any error
set -e

docker push $EXTERNAL_REGISTRY_ENDPOINT/$NAME:$CIRCLE_SHA1
