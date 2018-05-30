import os
import sys
import logging

logger = logging.getLogger(__name__)

SUPPORTED_FORMATS = [
    'image/jpeg'
]

MICROSOFT_API_URL = ''  # https://westcentralus.api.cognitive.microsoft.com/face/v1.0
MICROSOFT_API_KEY = ''


def get_url():
    try:
        global MICROSOFT_API_URL
        MICROSOFT_API_URL = os.environ['MICROSOFT_API_URL']
        assert MICROSOFT_API_URL
    except KeyError:
        logger.error('MICROSOFT_API_URL must be defined in your environment !')
        sys.exit(-1)
    except AssertionError:
        logger.error('MICROSOFT_API_URL cannot be blank !')
        sys.exit(-1)


def get_api_keys():
    try:
        global MICROSOFT_API_KEY
        MICROSOFT_API_KEY = os.environ['MICROSOFT_API_KEY']
        assert MICROSOFT_API_KEY
    except KeyError:
        logger.error('MICROSOFT_API_KEY must be defined in your environment !')
        sys.exit(-1)
    except AssertionError:
        logger.error('MICROSOFT_API_KEY cannot be blank !')
        sys.exit(-1)


get_url()
get_api_keys()
