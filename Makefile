.PHONY: clean system-packages python-packages install tests run all

# =============================================================================
# DECLARING VARIABLES
# =============================================================================

# DOCKERFILE PATH
PATH_DOCKERFILE=./Dockerfile

# DOCKERFILE CONTENTX
CONTEXT_DOCKERFILE=./

# CONTAINERS
DOCKER_CONTAINER_LIST:=$(shell docker ps -aq)

# =============================================================================
# DOCKER BUILD
# =============================================================================

build:
	docker image build --no-cache -t corona-api-tracker -f ${PATH_DOCKERFILE} ${CONTEXT_DOCKERFILE}

system:
	docker system prune -af

volume:
	docker volume prune -f

network:
	docker network prune -f

stop:
	docker stop ${DOCKER_CONTAINER_LIST}

remove:
	docker rm ${DOCKER_CONTAINER_LIST}

# =============================================================================
# DOCKER-COMPOSE
# =============================================================================

compose:
	docker-compose up --build

back:
	docker-compose up --build -d

down:
	docker-compose down

# =============================================================================
# PYTHON
# =============================================================================
	
clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python-pip -y

python-packages:
	pip install -r requirements.txt

install: system-packages python-packages

run:
	python code/python.py

all: clean install run
