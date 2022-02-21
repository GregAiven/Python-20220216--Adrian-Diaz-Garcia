#!/bin/bash
set -e
# This script waits for postgresql to startup and runs the consumer after that
PYTHONPATH=$PYTHONPATH:/app/monitor python -m etl