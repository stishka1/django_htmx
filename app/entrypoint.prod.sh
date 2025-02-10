#!/bin/sh
#Данный файл необходим чтобы проверить работоспособность PostgreSQL перед применением миграции и запуском сервера Gunicorn.

if [ "$DATABASE" = "postgres" ]
then
    echo "Postgres еще не запущен..."

    # Проверяем доступность хоста и порта
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 1
    done

    echo "PostgreSQL запущен"
fi

exec "$@"