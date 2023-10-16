#!/bin/bash
PROJECT_PATH=/home/ec2-user/
cd ${PROJECT_PATH}
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 279381197488.dkr.ecr.ap-northeast-2.amazonaws.com
docker-compose pull