include ../Makefile

STACKNAME:=osparc_dask

.PHONY: init up down

init:
	docker swarm init

up:
	docker-compose -f docker-compose-base.yml -f docker-compose-daskdev.yml config > docker-compose.yml
	docker stack deploy --compose-file docker-compose.yml ${STACKNAME}

up-sidecars:
	docker-compose -f docker-compose-base.yml -f docker-compose-sidecars.yml config > docker-compose.yml
	docker stack deploy --compose-file docker-compose.yml ${STACKNAME}

down:
	docker stack rm ${STACKNAME}
