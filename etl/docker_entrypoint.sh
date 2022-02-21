#!/bin/bash
set -e

# This script waits for postgresql to startup and runs the consumer after that
echo "Waiting for services to be available...." \
&& /app/etl/dockerize -wait tcp://${KAFKA_BOOTSTRAP_SERVER}  -timeout 60s \
&& /app/etl/dockerize -wait tcp://${DB_HOST}:${DB_PORT}  -timeout 60s \
&& echo "All services are up and running!"


"$@"
