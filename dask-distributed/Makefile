include ../Makefile

STACKNAME:=osparc_dask
TEMP_DIR := $(shell mktemp -d -t dask-docker-XXX)

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


PHONY: build-dask
#
# NOTE:  At this moment, this does not seem to work https://docs.docker.com/engine/reference/commandline/build/
# export DOCKER_BUILDKIT=0; docker build --tag local/dask:master https://github.com/dask/dask-docker.git#:base
#
build-dask: # builds official dask container from master branch repo
	git clone --depth 1 https://github.com/dask/dask-docker.git ${TEMP_DIR} && \
	docker build --tag local/dask:master ${TEMP_DIR}/base && \
	rm -rf ${TEMP_DIR}