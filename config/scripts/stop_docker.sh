#!/bin/bash

containers=$(docker ps -q)
ehco "컨테이너 종료"
if [ -n "$containers" ]; then
    docker stop $containers
fi
