install:
	poetry install

dev:
	poetry run python manage.py runserver 0.0.0.0:$(PORT)

build:
	./build.sh

messagesparse:
		poetry run django-admin makemessages -l ru

transmessages:
		poetry run django-admin compilemessages

PORT ?= 8000

start:
	poetry run gunicorn task_manager.wsgi:application

migration:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

check:
	poetry run flake8 task_manager/
