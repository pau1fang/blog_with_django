FROM python:3

ENV PYTHONUNBUFFERED=1
ENV BLOG_MYSQL_DATABASE blog_with_django
ENV BLOG_MYSQL_USER root

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
