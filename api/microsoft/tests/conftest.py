import pytest


@pytest.fixture()
def analyse_picture_result():
    return {
        'emotion': 'happiness',
        'percent': 1.0
    }
