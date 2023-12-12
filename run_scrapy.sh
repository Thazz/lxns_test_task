#!/bin/bash

RETRIES=10
until pg_isready -h $DB_HOST -U $DB_USER -d $DB_NAME > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
  echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
  sleep 1
done

echo "postgres server ready, starting spider"

scrapy crawl estates --loglevel=INFO
