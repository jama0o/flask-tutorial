from os.path import abspath, dirname, join
# Define the application directory
BASE_DIR = dirname(dirname(abspath(__file__)))
# Media dir
MEDIA_DIR = join(BASE_DIR, 'media')
POSTS_IMAGES_DIR = join(MEDIA_DIR, 'posts')
# instance/config.py
SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/miniblog'
ITEMS_PER_PAGE = 3
# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''
# Configuración del email
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'tfgcristianmg@gmail.com'
MAIL_PASSWORD = 'lohoafyxqybgzklq'
DONT_REPLY_FROM_EMAIL = '(CristianTFG, fgcristianmg@gmail.com)'
ADMINS = ('tfgcristianmg@gmail.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False