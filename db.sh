#! /bin/bash

set -e

psql service=admin --command="DROP DATABASE IF EXISTS blog;"
psql service=admin --command="CREATE DATABASE blog;"

python manage.py makemigrations
python manage.py migrate

python manage.py sample_db
