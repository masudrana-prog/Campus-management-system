#!/bin/bash
echo "🎓 Starting CampusHub..."
python manage.py migrate --run-syncdb
python manage.py seed_data
python manage.py runserver
