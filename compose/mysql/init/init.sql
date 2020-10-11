# compose/mysql/init/init.sql
GRANT ALL PRIVILEGES ON blog_with_django.* TO dbuser@"%" IDENTIFIED BY "password";
FLUSH PRIVILEGES;