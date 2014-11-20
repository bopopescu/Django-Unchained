# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG')
TEMPLATE_DEBUG = DEBUG

dirname = os.path.dirname
SITE_ROOT = os.path.realpath(dirname(dirname(__file__)))
PROJECT_ROOT = os.path.realpath(dirname(__file__))

#MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../../web/media').replace('\\','/')

# An iterable of filesystem directories to check when loading Django templates
# Search path.
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_=)&43))g8#qb6xjsrna$rm06)-dk==j1jre7w9-w5xz@zpik)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Applications

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_handlebars',
    'jstemplate',
    'searcher', # new app named searcher
    'tastypie',	# easy api wrapper     
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'snippetscream.ProfileMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES={'default':dj_database_url.config(),}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(SITE_ROOT,'statics')
MEDIA_ROOT = os.path.join(SITE_ROOT,'media')
#STATIC_URL = '/static/'



#AWS_ACCESS_KEY='AKIAIHKZPJBEJZR34IIA'
#AWS_SECRET_ACCESS_KEY='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'
#AWS_STORAGE_BUCKET_NAME='atlantis-smd'

#if os.environ.get('USE_S3') == 'off':
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

#else:
#    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')


#    DEFAULT_FILE_STORAGE = 'atlantis.s3utils.MediaRootS3BotoStorage'
#    STATICFILES_STORAGE = 'atlantis.s3utils.StaticRootS3BotoStorage'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
	os.path.join(SITE_ROOT,'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)




# Media files such as images
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/runserver.log',
            'formatter': 'simple'
            },
        },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
            },
        }
    }

if DEBUG:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']


# Execute to the file custom_settings.py for more settings                       
                                                                                 
try:                                                                             
   execfile(os.path.join(PROJECT_ROOT, 'custom_settings.py'))                    
except IOError:                                                                  
   pass                                                                          

