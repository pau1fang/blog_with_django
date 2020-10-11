FROM python:3

ENV PYTHONUNBUFFERED=1
ENV BLOG_MYSQL_DATABASE blog_with_django
ENV BLOG_MYSQL_USER dbuser
ENV BLOG_MYSQL_PASSWORD password

COPY pip.conf /root/.pip/pip.conf
RUN mkdir -p /code/blog_with_django
WORKDIR /code/blog_with_django
COPY . /code/blog_with_django/
RUN pip install -r requirements.txt