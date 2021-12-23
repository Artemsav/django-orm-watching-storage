import os
from dotenv import load_dotenv, find_dotenv
from environs import Env
import dj_database_url

load_dotenv(find_dotenv(),override=True)
env = Env()
env.read_env()


DATABASE_URL = os.getenv('DATABASE_URL')

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}

INSTALLED_APPS = ['datacenter']

DEBUG = env.bool('DEBUG', default=False)

SECRET_KEY = os.getenv('SECRET_KEY')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


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
