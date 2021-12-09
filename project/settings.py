import os
from dotenv import load_dotenv
from pathlib import Path
from environs import Env

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path,override=True)
env = Env()
env.read_env()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

DEBUG = env.bool("DEBUG", default=False)
print(os.getenv('USER'))

SECRET_KEY = os.getenv('SECRET_KEY')

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
