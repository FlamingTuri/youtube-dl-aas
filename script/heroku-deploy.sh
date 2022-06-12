#!/bin/bash

heroku login

heroku container:login

APP_NAME=youtube-dl-aas

IMAGE_NAME="python/$APP_NAME"

docker build -f Dockerfile.py -t "$IMAGE_NAME" .

REGISTRY_NAME="registry.heroku.com/$APP_NAME/web"

docker tag "$IMAGE_NAME" "$REGISTRY_NAME"
docker push "$REGISTRY_NAME"

heroku container:release web -a "$APP_NAME"

docker image prune -f
