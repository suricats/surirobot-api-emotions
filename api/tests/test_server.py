from flask import url_for
from unittest.mock import patch


def test_docs_redirect(client):
    res = client.get(url_for('index'))
    assert res.status_code == 301


def test_swagger_file(client):
    res = client.get(url_for('swagger_file'))
    assert res.status_code == 200


@patch('api.server.open')
def test_swagger_file_not_found(mock_open, client):
    mock_open.side_effect = FileNotFoundError()
    res = client.get(url_for('swagger_file'))
    assert res.status_code == 404
