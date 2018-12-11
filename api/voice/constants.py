import os
import sys
import logging

logger = logging.getLogger(__name__)


BEYOND_API_URL = ''
BEYOND_API_KEY = ''


def get_url():
    try:
        global BEYOND_API_URL
        BEYOND_API_URL = os.environ['BEYOND_API_URL']
        assert BEYOND_API_URL
    except KeyError:
        logger.error('BEYOND_API_URL must be defined in your environment !')
        sys.exit(-1)
    except AssertionError:
        logger.error('BEYOND_API_URL cannot be blank !')
        sys.exit(-1)


def get_api_keys():
    try:
        global BEYOND_API_KEY
        BEYOND_KEY = os.environ['BEYOND_API_KEY']
        assert BEYOND_API_KEY
    except KeyError:
        logger.error('BEYOND_API_KEY must be defined in your environment !')
        sys.exit(-1)
    except AssertionError:
        logger.error('BEYOND_API_KEY cannot be blank !')
        sys.exit(-1)


get_url()
get_api_keys()
