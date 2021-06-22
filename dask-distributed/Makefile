include ../Makefile

STACKNAME:=osparc_dask

.PHONY: init up down

init:
	docker swarm init

up:
	docker stack deploy --compose-file docker-compose.yml ${STACKNAME}

up-local:
	docker stack deploy --compose-file docker-compose-local.yml ${STACKNAME}


down:
	docker stack rm ${STACKNAME}
