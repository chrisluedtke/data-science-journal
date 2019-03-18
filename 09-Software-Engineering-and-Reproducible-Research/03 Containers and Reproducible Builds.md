# Containers and Reproducible Builds

## Learning Objectives

- Launch Docker containers and access/execute programs on them
- Create/customize a Dockerfile to build a basic custom container

## Before Lecture

- If you have Linux, MacOS Sierra or newer or Windows 10 Pro, install
  [Docker Desktop](https://www.docker.com/products/docker-desktop)
- If you have older MacOS, Windows 10 Home, or older Windows, install
  [Docker Toolbox](https://docs.docker.com/toolbox/overview/)
- If you're unable to locally install Docker, sign up for an account at
  [Docker Hub](https://hub.docker.com/)

## Live Lecture Task

Working with Docker is tricky - we'll step through a complete workflow live, and
answer questions that arise. In-depth debugging should be done 1:1 with PMs
after lecture.

## Assignment

Install and run code from your `lambdata` package inside a Docker container.
This is a relatively simple baseline to support the variety of local workflows
students will have.

## Resources and Stretch Goals

If your local installation isn't working, you can use the [Play with Docker
Classroom](https://training.play-with-docker.com/) - a Docker Hub account will
let you try Docker and spin up containers from your browser. They are
*temporary* (will go away when you leave the page), and editing the `Dockerfile`
will be a bit cumbersome, but we'll show how to in class.

The [official Docker documentation](https://docs.docker.com/) is extremely
thorough and worth checking out. For a particular stretch goal, explore
[Docker Compose](https://docs.docker.com/compose/), a powerful approach to
combining containers (e.g. you can run a local webapp and database together).

Explore [Hands-On Machine Learning in Docker](https://github.com/ageron/handson-ml/tree/master/docker),
a prebuilt Docker container with all sorts of DS/ML goodies. By using Docker you
can get up and running with sophisticated systems remarkably quickly.

Want to better understand the difference between VMs ("heavy") and containers
("light")? [This blog post](https://www.backblaze.com/blog/vm-vs-containers/)
highlights and summarizes the benefits and use cases of both.
