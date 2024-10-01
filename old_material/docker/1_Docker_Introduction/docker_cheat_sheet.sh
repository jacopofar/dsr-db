#!/usr/bin/env bash


# List all docker images
docker images

# Pull a docker image
docker pull mysql:5.7

# List all running containers
docker ps

# List all running and stopped containers
docker ps -a 

# Start a container from an image
docker run -it --rm mysql:5.7 /bin/bash

# Execute a command in an already running container 
docker exec -it --rm <container-name-or-id> /bin/bash

# Stop a running container from the outside
docker stop <container-name-or-id>
