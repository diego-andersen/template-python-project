run
	docker compose -f docker-compose.prod.yaml -d up --pull always

stop
	docker compose -f docker-compose.prod.yaml down

run_dev
	docker compose -f docker-compose.dev.yaml up --build

build
	docker compose -f docker-compose.dev.yaml build

build_and_push
	docker compose -f docker-compose.dev.yaml build
	docker compose -f docker-compose.dev.yaml push
	docker image prune -f
