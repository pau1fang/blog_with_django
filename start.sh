#!/bin/bash
python3 manage.py collectstatic --noinput&&
python3 manage.py makemigrations&&
python3 manage.py migrate&&
uwsgi --ini /code/blog_with_django/uwsgi.ini