# NABI 

Django-Web Application with G-Authenication and Testing with Docker Container

### Requirements :

Python 3+ | Django | PostgreSQL | Docker | Windows IDE | ubuntu

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

![2018-08-02 4 _li](https://user-images.githubusercontent.com/41096204/43567155-d22aa656-95fe-11e8-9734-7bfbf0c4c366.jpg)


Logging out and entering with another administrators email :

![2018-08-02 9 _li](https://user-images.githubusercontent.com/41096204/43567313-570075a4-95ff-11e8-99b5-b3f59817d7f6.jpg)

As the above image also states that only the administrator who added the client can delete or reedit the same client, other administrators can only view the client record.

Also developed a file format for administrators to be recorded on the django admin :

![2018-08-02 6 _li](https://user-images.githubusercontent.com/41096204/43567483-f0c8ae86-95ff-11e8-9515-f520c34b02b0.jpg)

### Setup Virtual Box Installing Ubuntu with graphical user interface/terminal or Any other System you wish to install :

![ubuntuinstallation](https://user-images.githubusercontent.com/41096204/43659622-8ef0b984-972a-11e8-8fa5-ef0ad010ba5b.png)

After installation of Virtual Box and Download an Ubuntu Image file which you wish to run your system with.

After downloading you can setup to run your image file to VB and create a space within your HD to enable you to use variety of applications and tools within the VB environment.

### Open terminal window within ubunto graphic user interface and install below

1) Install Docker

wget -qO- https://get.docker.com/ | sh

2) Permisson for all users to use docker

sudo usermod -aG docker $(whoami)

3) Install pip forpython 3

sudo apt-get install python3-pip -y

4) Install docker-compose

pip3 install docker-compose

5) Run docker-compose services
Open Terminal project/folder where manage.py is located then type

docker-compose up

![docker_compose_up](https://user-images.githubusercontent.com/41096204/43679685-a84a5c6e-97f7-11e8-88a8-869d7dff9603.png)

docker-compose up -d

6) Run Django project

### Only run the below the first time ( you must also make migrations)

docker-compose run webpy python3 manange.py makemigrations 

docker-compose run webpy python3 manage.py migrate

docker-compose run webpy python3 manage.py createsuperuser

7) Everytime you wish to run your app

docker-compose run webpy python3 manage.py runserver

![nabi_admin](https://user-images.githubusercontent.com/41096204/43679705-28d6ea00-97f8-11e8-888e-ace5e586f138.png)

open link in your browser : http://127.0.0.1:8000/

![nabi user area](https://user-images.githubusercontent.com/41096204/43679752-d6c2781e-97f8-11e8-8056-2b3f24d80eb7.png)

administration area of app

![inkedadmin_li](https://user-images.githubusercontent.com/41096204/43679762-18a46008-97f9-11e8-8eb3-eb178483170d.jpg)

Django admin 

8) Shutting down container by docker-compose down

![docker-compose-down](https://user-images.githubusercontent.com/41096204/43681337-64a7f79c-981e-11e8-9807-3c6446d31de0.png)

### Also note that settings.py needs to changed for the specific database used, and port; localhost should be the same name as per docker-compose.yml file

### Requirements for Docker running with Windows/Commandline or IDE : 

1) Stop docker-compose Services

Open Terminal inside Project Folder Where manage.py is located

docker-compose down

2) Start docker-compose Services

Open Terminal inside Project Folder Where manage.py is located

docker-compose up -d

3) Run Django project

### When you run this program 1st time you must make migrations
### Only for 1st Time

docker-compose run webpy python manage.py makemigrations

docker-compose run webpy python manage.py migrate

docker-compose run webpy python manage.py createsuperuser

### Every Time you want to run your apps

docker-compose run webpy python manage.py runserver 

Open this link in your Browser http://127.0.0.1:8000/

4) If Server Not Running Properly

If your Server not Work Properly Again Use these Commands

docker-compose down

docker-compose up
