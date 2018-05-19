import os
import sys
import logging

logger = logging.getLogger(__name__)

SUPPORTED_FORMATS = [
    'image/jpeg'
]

MICROSOFT_API_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
MICROSOFT_API_KEY = ''


try:
    MICROSOFT_API_KEY = os.environ['MICROSOFT_API_KEY']
    assert MICROSOFT_API_KEY
except (KeyError, AssertionError):
    logger.error('MICROSOFT_API_KEY must be defined in your environment !')
    sys.exit(-1)
