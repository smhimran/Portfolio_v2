import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '*1065%flo-7ip#4ik@j_fhct^hcz)ahf5&ub1s^$)j9q)1mf*w'

DEBUG = False

ALLOWED_HOSTS = ['smhimran.herokuapp.com', '127.0.0.1']

CLOUDINARY_CLOUD_NAME = "portfi"
CLOUDINARY_API_KEY = "599826876122524"
CLOUDINARY_API_SECRET = "ZJFc0VbRZ4Br3NjSyklySu_jj9w"

DB_CONFIG = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}


