import logging
from flask import Blueprint, request, jsonify

from api.exceptions import BadHeaderException, MissingHeaderException, APIException
from api.microsoft.helpers import microsoft_analyse_picture
from api.microsoft.constants import SUPPORTED_FORMATS

emo_microsoft = Blueprint('emo_microsoft', __name__)
logger = logging.getLogger(__name__)


@emo_microsoft.route('/analyse', methods=['POST'])
def analyse():
    content_type = request.headers.get('Content-Type')
    if not content_type:
        return jsonify({'errors': [MissingHeaderException('Content-Type').to_dict()]}), MissingHeaderException.status_code

    if content_type not in SUPPORTED_FORMATS:
        return jsonify({'errors': [BadHeaderException('Content-Type', valid_values=SUPPORTED_FORMATS).to_dict()]}), BadHeaderException.status_code

    file = request.data

    try:
        res = microsoft_analyse_picture(file)
    except APIException as e:
        return jsonify({'errors': [e.to_dict()]}), e.status_code
    except Exception as e:
        logger.error(e)
        return jsonify({'errors': [APIException().to_dict()]}), 500

    return jsonify(res), 200
