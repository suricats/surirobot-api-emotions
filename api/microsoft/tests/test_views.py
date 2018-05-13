import json
from mock import patch, Mock
from flask import url_for

from api.exceptions import BadHeaderException, MissingHeaderException
from api.microsoft.constants import SUPPORTED_FORMATS


@patch('api.microsoft.views.microsoft_analyse_picture', autospec=True)
def test_analyse_picture_success(mock_microsoft_analyse_picture, client, happy_file, analyse_picture_result):
    mock_microsoft_analyse_picture.return_value = analyse_picture_result

    res = client.post(
        url_for('emo_microsoft.analyse'),
        content_type='image/jpeg',
        data=happy_file
    )

    assert res.status_code == 200
    assert sorted(json.loads(res.data).items()) == sorted(analyse_picture_result.items())
    assert mock_microsoft_analyse_picture.call_count == 1


@patch('api.microsoft.views.microsoft_analyse_picture', autospec=True)
def test_analyse_picture_bad_content_type(mock_microsoft_analyse_picture, client, happy_file):
    res = client.post(
        url_for('emo_microsoft.analyse'),
        content_type='image/xxx',
        data=happy_file
    )

    expected_result = {'errors': [BadHeaderException('Content-Type', valid_values=SUPPORTED_FORMATS).to_dict()]}

    assert res.status_code == 400
    assert sorted(json.loads(res.data).items()) == sorted(expected_result.items())
    assert mock_microsoft_analyse_picture.call_count == 0


@patch('api.microsoft.views.microsoft_analyse_picture', autospec=True)
def test_analyse_picture_missing_content_type(mock_microsoft_analyse_picture, client, happy_file):
    res = client.post(
        url_for('emo_microsoft.analyse'),
        data=happy_file
    )

    expected_result = {'errors': [MissingHeaderException('Content-Type').to_dict()]}

    assert res.status_code == 400
    assert sorted(json.loads(res.data).items()) == sorted(expected_result.items())
    assert mock_microsoft_analyse_picture.call_count == 0
