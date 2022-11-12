.PHONY: docker
launch:
	docker-compose up --build -d

launch_db:
	docker-compose up --build -d db

check:
	docker ps -a | grep "inflazia"

check_logs:
	docker logs -t inflazia_dashboard

check_exec:
	docker exec -it inflazia_dashboard /bin/bash

stop:
	docker-compose down

stop_clear:
	docker-compose down -v

clean_volumes:
	docker volume prune

.PHONY: python-check
python-check:
	poetry run black .
	poetry run flake8 .

test:
	poetry run pytest .