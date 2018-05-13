import pytest
import os
import io

from api.server import app as flask_app


@pytest.fixture()
def app():
    return flask_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def happy_file():
    filename = os.getcwd() + '/api/tests/fixtures/happy.jpeg'
    with io.open(filename, 'rb') as picture:
        file = picture.read()
    return file
