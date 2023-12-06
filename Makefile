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

test:
	poetry run python3 manage.py test

lint:
	poetry run flake8 task_manager

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report
	poetry run coverage xml

check:
	poetry run flake8 task_manager/
