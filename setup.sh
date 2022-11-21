#!/bin/bash
cd Model/
docker build --tag model-api-docker .
cd ../Web/
docker build --tag web-api-docker .
cd ../Data/
docker build --tag data-api-docker .
cd ..
docker-compose up -d 