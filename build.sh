#!/usr/bin/env bash
# Exits on error
set -o errexit

# Installs the dependencies
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate