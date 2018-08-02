# NABI 

Django-Web Application with G-Authenication and Testing with Docker Container

# Used and Requirements :

Python 3+

Django==2.1
PyJWT==1.6.4
bcrypt==3.1.4
certifi==2018.4.16
cffi==1.11.5
chardet==3.0.4
defusedxml==0.5.0
idna==2.7
oauthlib==2.1.0
psycopg2==2.7.5
pycparser==2.18
python-social-auth==0.3.6
python3-openid==3.1.0
pytz==2018.5
requests==2.19.1
requests-oauthlib==1.0.0
six==1.11.0
social-auth-app-django==2.1.0
social-auth-core==1.7.0
sqlparse==0.2.4
urllib3==1.23

# Pre-Setup

1) Ensure PostgreSQL is setup with a database running on your computer
2) Please adjust the name and login, password details in settings.py file (scroll to databases and make adjusted changes)
3) Install Docker on your computer 

# Setup for Python and Django

1) Install and activate a 'ENV' environment 
2) Open requirements.txt file for libraries and installation
3) then locate manage.py file directory
4) python manage.py makemigrations
5) python manage.py migrate
6) python manage.py runserver


