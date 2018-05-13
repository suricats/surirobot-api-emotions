import pytest

from api.microsoft.helpers import microsoft_analyse_picture


@pytest.mark.externalapi
def test_service_available(happy_file, analyse_picture_result):
    res = microsoft_analyse_picture(happy_file)

    assert sorted(analyse_picture_result.items()) == sorted(res.items())
