# POC `django-crontab` in docker
> a POC for using `django-crontab` in docker
> - python:3.11-alpine
> - python:3.11-bookworm

## Usage

`docker compose up -d`

> after the containers are up, there should be a new log entry every minute

### Check jobs from alpine

- http://localhost:8000/logs

### Check jobs from bookworm

- http://localhost:8001/logs
