from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$m+%&u8z+j)ok%kdizoa8vfd%rzxj%qu(i&5%6l2(@_m*=_*4h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'abroad',
        'USER': 'gregori',
        'PASSWORD': 'fender25',
        'HOST': 'localhost',  # Puedes reemplazarlo con la dirección de tu servidor PostgreSQL si es diferente.
        'PORT': '5432',       # El puerto predeterminado de PostgreSQL es 5432.
    }
}
import os

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('RAILWAY_PG_DB'),
#         'USER': os.getenv('RAILWAY_PG_USER'),
#         'PASSWORD': os.getenv('RAILWAY_PG_PASSWORD'),
#         'HOST': os.getenv('RAILWAY_PG_HOST'),
#         'PORT': os.getenv('RAILWAY_PG_PORT'),
#     }
# }