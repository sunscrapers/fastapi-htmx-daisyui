REQUIREMENTS_FILE = dev.txt

.PHONY: update-deps
update-deps:
	pip install -U pip && pip install pip-tools

	pip-compile requirements/base.in
	pip-compile requirements/dev.in

.PHONY: build
build:
	[ -f .env ] || cp example.env .env
	docker compose build --build-arg="REQUIREMENTS_FILE=$(REQUIREMENTS_FILE)"

.PHONY: up
up:
	make build
	docker compose up

.PHONY: down
down:
	docker compose down

.PHONY: attach
attach:
	docker attach fasthtmx_app

.PHONY: db-migrate
db-migrations:
	docker exec -it fasthtmx_app alembic -c app/models/alembic.ini revision --autogenerate

.PHONY: db-upgrade
db-migrate:
	docker exec -it fasthtmx_app alembic -c app/models/alembic.ini upgrade head

.PHONY: db-downgrade
db-downgrade:
	docker exec -it fasthtmx_app alembic -c app/models/alembic.ini downgrade -1

.PHONY: migration-history
migration-history:
	docker exec -it fasthtmx_app alembic -c app/models/alembic.ini history

.PHONY: bash
bash:
	docker exec -it fasthtmx_app bash

.PHONY: run-build
run-build:
	docker build . -f docker/Dockerfile -t fasthtmx_app:latest --build-arg="REQUIREMENTS_FILE=$(REQUIREMENTS_FILE)"

.PHONY: run
run:
	make run-build
	docker run --name fasthtmx_app -p 8000:8000 --rm --env-file .env -it fasthtmx_app:latest

.PHONY: run-tests
run-tests:
	make run-build
	docker run --name fasthtmx_app -p 8000:8000 --rm --env-file .env -it fasthtmx_app:latest python -m pytest app -s --verbose

.PHONY: tests
tests:
	docker exec -it fasthtmx_app python -m pytest app/tests -s --verbose

.PHONY: bootstrap
bootstrap:
	docker exec -it fasthtmx_app python app/commands/bootstrap.py

.PHONY: e2e-tests-build
e2e-tests-build:
	docker build . -f e2e_tests/Dockerfile -t tests_e2e:latest

.PHONY: e2e-tests-bash
e2e-tests-bash:
	make e2e-tests-build
	docker run --name tests_e2e --network="host" --rm -it tests_e2e:latest bash

.PHONY: e2e-tests
e2e-tests:
	make e2e-tests-build
	docker run --name tests_e2e --network="host" --rm -it tests_e2e:latest pytest tests -s --base-url http://localhost:8000
