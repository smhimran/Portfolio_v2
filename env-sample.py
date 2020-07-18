import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'secretkey'

DEBUG = True

ALLOWED_HOSTS = ['*']

CLOUDINARY_CLOUD_NAME = "Cloudinary Cloud name"
CLOUDINARY_API_KEY = "Coudinary API"
CLOUDINARY_API_SECRET = "Coudinary API secrete"

DB_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}


