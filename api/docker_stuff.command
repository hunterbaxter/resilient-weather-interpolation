#!/bin/sh
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
docker build -t weather_api:latest .
docker tag weather_api:latest alexpena9291/cloud_computing:weather_api
docker push alexpena9291/cloud_computing:weather_api