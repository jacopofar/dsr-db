# Building Docker Images

## Basics: How is an image created?

To build your own Docker images, you need to create a [Dockerfile](https://docs.docker.com/engine/reference/builder/).

This file acts as a recipe, creating the image step by step.

In this folder, we have already included a `Dockerfile`. Take a look.

When building the image, `ADD` and `COPY` can use files that we have in the local filesystem.

NOTE: commands in the Dockerfile cannot be interactive. This is why there's a `-y` flag in apt arguments.

And when you are ready to build, run the following command.

```
docker build -t custom-dsr .
```

This looks for a file calle `Dockerfile` in the current directory, bilds the image and tags it as `custom-dsr`

```
docker run --rm custom-dsr
```

## Exercise: Creating your own Docker image

- Use this Dockerfile as reference
- Use `ubuntu:20.04` as base image
- Install python 3.9 in it
- Create a python file `hello.py` that outputs "Hello from Python"
- Make sure that this python file is executed on running the image
