export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml cat-stack
docker service update --replicas 3 cat-stack_front-end
docker service update --replicas 3 cat-stack_front-end