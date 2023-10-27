install:
	poetry install

check:
	poetry check

PORT ?= 8000
dev:
	poetry run python manage.py runserver 0.0.0.0:$(PORT)

start:
	poetry run gunicorn task_manager.wsgi