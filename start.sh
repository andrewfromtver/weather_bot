#! /bin/bash

docker build -t weather-bot:production . > build.log
docker run --rm -it weather-bot:production&
