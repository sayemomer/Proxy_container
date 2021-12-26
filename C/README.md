
# requirements

* docker

# Setup

* Start with Docker:
    ```$ docker build -t taskc . ```
    ```$ docker run -p 5000:5000 taskc```

* docker run -p 5000:5000 taskc -d : Detach it from running in background
* docker ps: lists the containers that are still running. Add the -a switch in order to see containers that have stopped
* docker logs: retrieves the logs of a container, even when it has stopped
* docker inspect: gets detailed information about a running or stopped container
* docker stop: stops a container that is still running
* docker rm: deletes a container
* docker container prune -f: This is the equivalent of running one docker rm command for each stopped container.
