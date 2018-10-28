from .base import *

DEBUG = False
PROD = True

ALLOWED_HOSTS = ['*']

# CORS_ORIGIN_WHITELIST = (
#     'frontsergibucket.s3-website-eu-west-1.amazonaws.com',
# )
# CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'db.sqlite3'),
    }
}

# BASE_URL = 'http://autoserviciosBBVA-devQA.eu-central-1.elasticbeanstalk.com'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ' [%(asctime)s] [%(levelname)s] [%(name)s] %(message)s'
        },
        'simple': {
            'format': ' %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join('/var/log/app-logs/messages.log')
        },
        'file_errors': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join('/var/log/app-logs/errors.log')
        },
    },
    'loggers': {
        'main': {
            'handlers': ['console', 'file', 'file_errors'],
            'level': 'DEBUG'
        }
    }
}
