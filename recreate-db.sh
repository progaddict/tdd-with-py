#!/usr/bin/env bash

rm db.sqlite3 && python manage.py migrate --noinput
