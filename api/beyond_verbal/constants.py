import os
import sys
import logging

logger = logging.getLogger(__name__)


BEYONDVERBAL_API_URL = ''
BEYONDVERBAL_TOKEN_URL = ''
BEYONDVERBAL_API_KEY = ''

SUPPORTED_FORMATS = [
    'audio/x-wav'
]

def get_url():
    try:
        global BEYONDVERBAL_API_URL
        BEYONDVERBAL_API_URL = os.environ.get('BEYONDVERBAL_API_URL')
        assert BEYONDVERBAL_API_URL
    except KeyError:
        logger.error('BEYONDVERBAL_API_URL must be defined in your environment !')
        sys.exit(-1)
    except AssertionError:
        logger.error('BEYONDVERBAL_API_URL cannot be blank !')
        sys.exit(-1)

def get_url_token():
    try:
        global BEYONDVERBAL_TOKEN_URL
        BEYONDVERBAL_TOKEN_URL = os.environ['BEYONDVERBAL_TOKEN_URL']
        assert BEYONDVERBAL_TOKEN_URL
    except KeyError:
        logger.error('BEYONDVERBAL_TOKEN_URL must be defined in your environment !')
        sys.exit(-1)
    except AssertionError:
        logger.error('BEYONDVERBAL_TOKEN_URL cannot be blank !')
        sys.exit(-1)

def get_api_keys():
    try:
        global BEYONDVERBAL_API_KEY
        BEYONDVERBAL_API_KEY = os.environ['BEYONDVERBAL_API_KEY']
        assert BEYONDVERBAL_API_KEY
    except KeyError:
        logger.error('BEYONDVERBAL_API_KEY must be defined in your environment !')
        sys.exit(-1)
    except AssertionError:
        logger.error('BEYONDVERBAL_API_KEY cannot be blank !')
        sys.exit(-1)


get_url()
get_url_token()
get_api_keys()
