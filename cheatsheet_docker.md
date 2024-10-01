## Docker cheatshet

Image name: `username/image:tag`
the default tag is `latest`, username is omitted on official images.

Image commands:

* `docker pull X` pulls image X
* `docker images` list downloaded images
* `docker rmi X` deletes image X (identified by name or id)

Container commands:

* `docker ps` lists running containers
* `docker ps -a` lists also stopped containers
* `docker stop X` stops a container X (it tells it to quit and waits)
* `docker kill X` stops a container X without waiting
* `docker rm` deletes a stopped container (not needed when using `--rm` with docker run)
* `docker cp container:path path` copies file to/from a container
* `docker exec -it X Y` runs command Y on already running container X
* `docker attach` connects to a container already running but detached
* `docker run` starts a container, many flags:
  * `-it` interactive mode
  * `-d` detached, opposite as `-it`
  * `--rm` deletes the container when exiting
  * `--name X` name X the container, if not provided a random name is used
  * `-v X:Y` mounts volume or absolute path X under the path Y.
  * `docker run X Y` runs command Y on image X, if omitted runs the default
   command defined in image metadata
  * `docker system prune` removes unused images and containers
Build commands:

* `docker build .` builds an image from the Dockerfile in this folder
* `docker build -t X .` builds an image and names it X
* `docker tag X Y` gives a name Y to image X, X can be the hash

In the Dockerfile:

* `FROM X` starts from a base image, usually the first command
* `RUN X` runs a command that will have an effect on the final image
* `COPY X Y` copies relative path X in the image path Y
* `ADD X Y` same as `COPY`, but X can be an URL or an archive to decompressed
