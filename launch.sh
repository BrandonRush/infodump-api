#!/bin/bash/

docker build -t infodump-api .

docker run -d -p 127.0.0.1:8000:8000 --name app infodump-api

sleep 60

docker exec python manage.py runserver 0.0.0.0:8000
