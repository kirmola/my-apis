from api.settings_base import *
from django.core.management.utils import get_random_secret_key

DEBUG = False

MIDDLEWARE += [

]

INSTALLED_APPS += [
    
]

ALLOWED_HOSTS = [".kirmola.dev", ".vercel.app"]

SECRET_KEY = get_random_secret_key()