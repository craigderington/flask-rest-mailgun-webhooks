import os

# base_dir
basedir = os.path.abspath(os.path.dirname(__file__))

# debug
DEBUG = True

# Your App secret key
SECRET_KEY = os.urandom(64)

# Mail
MAIL_USERNAME = 'sender@email.com'
MAIL_PASSWORD = '****your-password***'
MAIL_DEFAULT_SENDER = 'Flask RESTFul Webhooks <webhooks@mailgun.org>'

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@localhost/database_name'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json', 'pickle']

# App name
APP_NAME = "Flask RESTFul MailGun WebHook API"

# Mail Gun
MAILGUN_API_KEY = 'your-mail-gun-key'.encode('utf-8')

