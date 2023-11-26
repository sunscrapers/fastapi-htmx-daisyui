.PHONY: update-deps build up down attach bash run-build run tests
update-deps:
	pip install -U pip && pip install pip-tools

	pip-compile requirements/base.in
	pip-compile requirements/dev.in

REQUIREMENTS_FILE = dev.txt
build:
	[ -f .env ] || cp example.env .env
	docker compose build --build-arg="REQUIREMENTS_FILE=$(REQUIREMENTS_FILE)"

up:
	make build
	docker compose up

down:
	docker compose down

attach:
	docker attach fasthtmx_app

bash:
	docker exec -it fasthtmx_app bash

run-build:
	docker build . -f docker/Dockerfile -t fasthtmx_app:latest --build-arg="REQUIREMENTS_FILE=$(REQUIREMENTS_FILE)"

run:
	docker run --name fasthtmx_app -p 8000:8000 --rm --env-file .env -it fasthtmx_app:latest

tests:
	docker exec -it fasthtmx_app python -m pytest app -s --verbose
