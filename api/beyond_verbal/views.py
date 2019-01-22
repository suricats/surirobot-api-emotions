# -*- coding: utf-8 -*-
"""
** Affective IT for SuriRobot
** 
** Made by Alexandre Brun
** Login   <alexandre.brun@suricats-consulting.com>
** 
** Started on  Wed Oct 17 10:51:11 2017 Alexandre Brun
"""

import logging
from flask import Blueprint, request, jsonify

from api.exceptions import BadHeaderException, MissingHeaderException, BaseAPIException, UnknownAPIException
from api.beyond_verbal.helpers import beyond_verbal_analyse_voice
from api.beyond_verbal.constants import SUPPORTED_FORMATS

emo_beyond_verbal = Blueprint('emo_beyond_verbal', __name__)
logger = logging.getLogger(__name__)


@emo_beyond_verbal.route('/analyse', methods=['POST'])
def analyse():
    content_type = request.headers.get('Content-Type')
    if not content_type:
        return jsonify({'errors': [MissingHeaderException('Content-Type').to_dict()]}), MissingHeaderException.status_code

    if content_type not in SUPPORTED_FORMATS:
        return jsonify({
            'errors': [BadHeaderException('Content-Type', valid_values=SUPPORTED_FORMATS).to_dict()]
        }), BadHeaderException.status_code

    file = request.data

    try:
        res = beyond_verbal_analyse_voice(file)
    except BaseAPIException as e:
        return jsonify({'errors': [e.to_dict()]}), e.status_code
    except Exception as e:
        logger.error(e)
        return jsonify({'errors': [UnknownAPIException().to_dict()]}), 500

    return jsonify(res), 200

#data = getAnalysis("755df2e5-10d6-41d1-8f12-3e1b34325261","samples/output.wav")
#print(json.dumps(data, sort_keys=True, indent=4))
