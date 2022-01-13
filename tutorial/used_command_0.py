# 0 quickstart

# Create a virtual environment to isolate our package dependencies locally
# python3 - m venv env
# source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
# pip install django
# pip install djangorestframework

# Set up a new project with a single application
# django-admin startproject tutorial .  # Note the trailing '.' character
# cd tutorial
# django-admin startapp quickstart

# python manage.py migrate
# python manage.py createsuperuser - -email admin@example.com - -username admin
# python manage.py runserver

# http: // 127.0.0.1: 8000/
# http: // 127.0.0.1: 8000/quick/users/
# http: // 127.0.0.1: 8000/api-auth/logout/
# http: // 127.0.0.1: 8000/admin/login/
