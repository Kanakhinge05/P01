#!/bin/bash

aws s3 cp s3://devops-artifacts-kanak/myapp_v1.tar .
docker load < myapp_v1.tar
docker stop $(docker ps -q)
docker run -d -p 80:80 myapp:v1
