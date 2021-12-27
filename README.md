
# Requirements

* python3

* pip3 

* virtualenv

* Post installation steps for linux: https://docs.docker.com/engine/install/linux-postinstall/

* Install docker engine on ubuntu: https://docs.docker.com/engine/install/ubuntu/

# Setup

* docker build -t task . : Build the docker file
* docker run --rm -it -p 5000:5000 task : Run the docker Image from registry
* docker run -p 5000:5000 taskc -d : running in background
* docker ps: lists the containers that are still running. Add the -a switch in order to see containers that have stopped
* docker logs: retrieves the logs of a container, even when it has stopped
* docker inspect: gets detailed information about a running or stopped container
* docker stop: stops a container that is still running
* docker rm: deletes a container
* docker container prune -f: This is the equivalent of running one docker rm command for each stopped container.
* docker image ls : See the images available locally.

### Publish the docker image

* docker tag task sayemomer/task

* docker login

* docker push sayemomer/task

## Run Without docker

* create vertualenv : $ virtualenv venv --python=python3  
* active vertualenv : $ source venv/bin/activate
* install dependencies: $ pip3 install -r requirements.txt
* Start the server: $ python3 main.py

# Sample I/O

* Input: http://192.168.0.106:5000/calculate?task=2\nSun%2010%20May%202015%2013:54:36%20-0700\nSun%2010%20May%202015%2013:54:36%20-0000\nSat%2002%20May%202015%2019:54:36%20+0530\nFri%2001%20May%202015%2013:54:36%20-0000

* Output: [25200, 88200]


