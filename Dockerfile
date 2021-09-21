FROM python:2
ADD Server_TCP.py /


#ADD THE PORT TO EXPOSE
EXPOSE 



CMD [ "python", "./Server_TCP.py" ]
