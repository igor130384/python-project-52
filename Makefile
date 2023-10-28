install:
	poetry install

dev:
	poetry run python manage.py runserver 0.0.0.0:$(PORT)

build:
	./build.sh


PORT ?= 8000

start:
	poetry run gunicorn task_manager.wsgi:application


check:
	poetry run flake8 task_manager/
