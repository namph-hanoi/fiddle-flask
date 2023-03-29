#!/bin/sh

# Todo: script to create table if there is no such table existing

flask db upgrade

exec gunicorn --bind 0.0.0.0:80 "app:create_app()"