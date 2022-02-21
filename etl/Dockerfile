FROM python:3.9-slim-buster as app
# Installing postgresql client
RUN apt-get update && apt-get install -y postgresql-client
RUN mkdir -p /app
WORKDIR /app
ADD requirements.txt /tmp/requirements.txt
ADD requirements_dev.txt /tmp/requirements_dev.txt
RUN pip install -r /tmp/requirements.txt
ADD . /app/etl

CMD /app/etl/docker_start.sh