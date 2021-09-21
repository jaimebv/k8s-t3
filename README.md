# k8s-t3

DOING we have a TCP written in python. The server and the client will be provided to you. The server runs in a deployment in k8s and the client must run externally. The server (internal to k8s) listens to port 15005. 
* Create a docker image called **tcp-k8s:v1** modifying the Dockerfile provided
* Based on the template used during the lab, create the required configuration files (.yaml).  Create 3 replicas 
* Type _kubectl describe service <<Your-service-name>>_ and explain what you see
* Based on the information gotten from C, modify the port of the **client.py** file and run it in a separated console to see the results 
