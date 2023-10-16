#!/bin/bash

python manage.py collectstatic --no-input
gunicorn sports_live.wsgi:application --bind 0.0.0.0:8000