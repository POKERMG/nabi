# NABI 

Django-Web Application with G-Authenication and Testing with Docker Container

### Requirements :

Python 3+ | Django | PostgreSQL | Docker

### Libraries :

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

### Pre-Setup :

1) Ensure PostgreSQL is setup with a database running on your computer
2) Please adjust the name and login, password details in settings.py file (scroll to databases and make adjusted changes)
3) Install Docker on your computer 

### Setup for Python and Django for running the application :

1) Install and activate a 'ENV' environment 
2) Open requirements.txt file for libraries and installation
3) then locate manage.py file directory
4) python manage.py makemigrations
5) python manage.py migrate
6) python manage.py runserver

After running the server you would have the authentication screen appear:

![2018-07-30 1](https://user-images.githubusercontent.com/41096204/43560533-f616b1ea-95e0-11e8-80c8-6e5af30403c9.png)

Once Google Authentication is clicked you would need to enter your google email :

![2018-08-02 7 _li](https://user-images.githubusercontent.com/41096204/43566858-e501e3da-95fd-11e8-9410-550d3e7cf6f3.jpg)

Adding client details :

![2018-08-02 4](https://user-images.githubusercontent.com/41096204/43567074-91c0ecce-95fe-11e8-8724-73b56ace9f3c.png)

Logging out and entering with another administrators email :



