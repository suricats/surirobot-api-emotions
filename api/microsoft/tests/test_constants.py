import os
from unittest.mock import patch

from api.microsoft.constants import get_api_keys, MICROSOFT_API_KEY, sys


def test_get_api_keys():
    assert MICROSOFT_API_KEY


@patch.object(sys, 'exit', autospec=True)
def test_get_api_keys_missing(mock_exit):
    mock_exit.return_value = None
    del os.environ['MICROSOFT_API_KEY']
    get_api_keys()
    assert mock_exit.call_count == 1


@patch.object(sys, 'exit', autospec=True)
def test_get_api_keys_blank(mock_exit):
    mock_exit.return_value = None
    os.environ['MICROSOFT_API_KEY'] = ''
    get_api_keys()
    assert mock_exit.call_count == 1
