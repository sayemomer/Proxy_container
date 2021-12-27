
# Problem

When users post an update on social media,such as a URL, image, status update etc., other users
in their network are able to view this new post on their news feed. Users can also see exactly when
the post was published, i.e, how many hours, minutes or seconds ago.
Since sometimes posts are published and viewed in different time zones, this can be confusing. You
are given two timestamps of one such post that a user can see on his newsfeed in the following
format:
**Day dd Mon yyyy hh:mm:ss +xxxx**
Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds)
between them.

## Input Format:

The first line contains T, the number of test cases.
Each test case contains 2 lines, representing time t1 and time t2.

## Constraints:
1. Input contains only valid timestamps
2. year<=3000

## Output Format:
Print the absolute difference (t1-t2) in seconds.

### Sample Input:
* 2
* Sun 10 May 2015 13:54:36 -0700
* Sun 10 May 2015 13:54:36 -0000
* Sat 02 May 2015 19:54:36 +0530
* Fri 01 May 2015 13:54:36 -0000

### Sample Output:
- 25200
- 88200

## Explanation:
In the first query, when we compare the time in UTC for both the time stamps, we see a difference of
7 hours. which is 7x3600 seconds or 25200 seconds.
Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for
that we have a difference of 1 day and 30 minutes. Or 24x3600+30x60 => 88200


# Task 

A python service which will take Task as an input(plain text with new line) through python
rest api. Output will be the same as Task response. Response will be an ordered json array
with the result.
Example: [ "25200", "88200" ]

Containerize(docker) and run at least two images so that any app instance can
provide the result as response. Also add node id from which node it is serving.
Example:
{
"id":"YOUR_NODE_ID",
"result":[ "25200", "88200"]
}


---
---




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


