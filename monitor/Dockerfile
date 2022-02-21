FROM python:3.9-slim-buster as app
RUN mkdir -p /app
WORKDIR /app
ADD requirements.txt /tmp/requirements.txt
ADD requirements_dev.txt /tmp/requirements_dev.txt
RUN pip install -r /tmp/requirements.txt
ADD . /app/monitor

CMD /app/monitor/docker_start.sh