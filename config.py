HOST = "127.0.0.1"
PORT = "4000"
# debug
DEBUG = True

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
DATABASE_CONFIG = {
    'host': 'localhost',
    'dbname': 'bbd',
    'user': 'postgres',
    'password': 'psql',
    'port': 5432
}

# multi thread rendering, cuz we can
THREADS_PER_PAGE = 2

# cross site protection on
CSRF_ENABLED = True
# secret is not so secret but its just a random project xD
CSRF_SESSION_KEY = "secret"

#ML vars
PREDICTOR = {
    'img_mean': [27.99144619, 19.51839209, 16.42992409],
    'img_std': [64.7680645, 47.09696396, 41.13751611],
    'img_target_size': (96, 128),
    'model_path': '/CNN/models/CNN_binary_v1.h5',
    'data_path': 'data/ISIC'
}
