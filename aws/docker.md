# Docker
Lets assume we are developing an app in our local machine Linux for that we required dependencies like ndoe v16 and for caching we need redis v6 and we downloaded that
lets assume we are working with team there are so many members and new one joined with mac machine so when he downloaded node.js latest version v20 and redis v7 the app may not work  and also the app we developed may work only with some cli commands so here there will be concept of docker

# Docker is useful to create containers
Container means the application code and their dependencies we can make them as a single unit and can be given to a fellow developer, so that we don't want to install the single dependenies seperately, we can deploy the whole unit once so that it can run without errors like it will install only node.js verson 16 and redis v7 and irrespective of machine it will work on any system like mac and linux

**Docker is a service/platform which is useful for building containers like to build containers/destroy containers and to update containers it will be helpful**

1. Contaiers are portable(can be shared from one machine to another one)
2. Containers are lightweight(easy to build/update and destroy)

# Docker Image
**Docker Image is actually a executable file**
This file contains the instruction of how we should build a conatiner
Using one image we can make multiple containers
When we say we share the conatiners, exactly we don't share the container we make the docker image and we share the docker image, with the help of this container image every one will build their own container

**Docker image is a static snapshot of what the application code and their dependencies are**

We can say Docker Image as class(which tells how the object should looks like) it says how the conatiners shoudl look like

**We can say container as a static instance of a docker image**

**Docker has Docker Hub where we upload our docker images like how we upload our code in GitHub**

We pull the docker image in to our machine using the command **docker pull hello-world** command with that we create the container

# Convert the docker image into conatiner and run that container
After pulling if you want to convert that image into container and run that container we use the command **docker run hello-world** here the hello-world is the name of the docaker image

# This is exactly from terminal
sahaanirban@Fasi-MacBook-Pro ~ % docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world
58dee6a49ef1: Pull complete 
Digest: sha256:7f4da0fc94bcece205a8c0b6f4d11c8196924654ffe5c4d1aa439b7f632048b2
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
sahaanirban@Fasi-MacBook-Pro ~ % docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

sahaanirban@Fasi-MacBook-Pro ~ % 

# Docker daemon
The Docker Daemon(called dockerd) is the background service that does all the actuall background work of Docker.When you run a Docker command, you're usually talking to the daemon, which manages docker images,containers,networks and volumes.

+----------------+
| Docker CLI     |   (docker run, docker ps, etc.)
+----------------+
         |
         | API request
         v
+----------------+
| Docker Daemon  |  (dockerd)
+----------------+
   |     |     |
   |     |     |
Containers Images Networks Volumes

# What is meant by -it command in docker
**docker run -it ubuntu bash**
-i=Interactive
-i stands for interactive 
It keeps the conatiner STDIN(input) open so that you can type commands into the container
-t=TTY
-t allocates a pseudo-terminal(TTY)
Together: -it
docker run -it ubuntu

This means:

Start an Ubuntu container and give me an interactive terminal inside it.

For example:

docker run -it ubuntu

**Simple understanding after we run that command our terminal points inside the conatiner**

After we run this -it command with ubuntu as docker image we now can make the directories install other dependencies and we can develop anything we want which will be inside the conatiner now not in our local 

We can exit from the conatiner terminal as well with command **exit**

and we stop the docker image with command **docker stop**

