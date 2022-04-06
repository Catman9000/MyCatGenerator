export MYSQL_ROOT_PASSWORD
docker stack deploy --compose-file docker-compose.yaml cat-stack
docker service update --replicas 3 animal-noises-stack_front-end
