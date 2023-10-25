docker stop $(docker ps -q)
docker container prune
docker volume prune
docker network prune
