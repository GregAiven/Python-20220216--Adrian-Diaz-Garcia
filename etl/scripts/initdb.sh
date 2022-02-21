#!/bin/bash
set -e

psql -h "$DB_HOST"  --username "$POSTGRES_USER" --dbname postgres -f etl/scripts/create_table.sql