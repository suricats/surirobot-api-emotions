import pytest
from mock import patch, Mock

from api.microsoft.helpers import microsoft_analyse_picture, requests
from api.exceptions import APIThrottlingException, InvalidCredentialsException, ExternalAPIException


@patch.object(requests, 'post', autospec=True)
def test_microsoft_analyse_picture_success(mock_post, happy_file):
    mock_post.return_value = Mock(status_code=200, json=lambda: [{'faceAttributes': {'emotion': {'happy': 0.7, 'sad': 0.3}}}])

    expected_result = {
        'emotion': 'happy',
        'percent': 0.7
    }
    result = microsoft_analyse_picture(happy_file)

    assert sorted(result.items()) == sorted(expected_result.items())


@patch.object(requests, 'post', autospec=True)
def test_microsoft_analyse_picture_throttling(mock_post, happy_file):
    mock_post.return_value = Mock(status_code=429)

    with pytest.raises(APIThrottlingException):
        microsoft_analyse_picture(happy_file)


@patch.object(requests, 'post', autospec=True)
def test_microsoft_analyse_picture_invalid_credentials(mock_post, happy_file):
    mock_post.return_value = Mock(status_code=401)

    with pytest.raises(InvalidCredentialsException):
        microsoft_analyse_picture(happy_file)


@patch.object(requests, 'post', autospec=True)
def test_microsoft_analyse_picture_unknown(mock_post, happy_file):
    mock_post.return_value = Mock(status_code=500)

    with pytest.raises(ExternalAPIException):
        microsoft_analyse_picture(happy_file)


@patch.object(requests, 'post', autospec=True)
def test_microsoft_analyse_picture_empty_emotion_field(mock_post, happy_file):
    mock_post.return_value = Mock(status_code=200, json=lambda: [{'faceAttributes': {'emotion': {}}}])

    with pytest.raises(ExternalAPIException):
        microsoft_analyse_picture(happy_file)


@patch.object(requests, 'post', autospec=True)
def test_microsoft_analyse_picture_incorrect_return(mock_post, happy_file):
    mock_post.return_value = Mock(status_code=200, json=lambda: [{}])

    with pytest.raises(ExternalAPIException):
        microsoft_analyse_picture(happy_file)


@pytest.mark.externalapi
def test_service_available(happy_file, analyse_picture_result):
    res = microsoft_analyse_picture(happy_file)

    assert sorted(analyse_picture_result.items()) == sorted(res.items())
