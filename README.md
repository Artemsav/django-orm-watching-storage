# Django-orm watching storage

## Project description

This is an internal repository for the Shining Bank employees. If you got into this repository by accident, then you will not be able to start it, since you do not have access to the database, but you can freely use the layout code or see how queries to the database are implemented.
The security console is a site that can connect to a remote database with visits and pass cards of our bank employees
To run the project you shall you the follwing command:

```bash
python3 manage.py runserver [addrport]
```

Starts a lightweight development web server on the local machine. By default, the server runs on port 8000 on the IP address 127.0.0.1. You can pass in an IP address and port number explicitly, more info on [Django docs](https://docs.djangoproject.com/en/4.0/ref/django-admin/)

## Installation

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

There is enviroment variables using in the application, you will need tp create .env file. A .env file is a text file containing key value pairs of all the environment variables required by the application. You can see example of it below:

```# example of environment variables defined inside a .env file
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME, more information you can find [here](https://github.com/jacobian/dj-database-url)
DEBUG='False', more information you can find in Djago documentation
SECRET_KEY='some string'
ALLOWED_HOSTS='hosts' or default '*', more information you can find in Djago documentation
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [Devman](https://dvmn.org)
