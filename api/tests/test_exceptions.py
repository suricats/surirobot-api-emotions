import pytest

from api.exceptions import APIThrottlingException, ExternalAPIException, InvalidCredentialsException, OperationFailedException, \
    BadParameterException, MissingParameterException, MissingHeaderException, BadHeaderException, UnknownAPIException


def test_exception_unknown_api_exception():
    expected_result = {
        'code': 'api_error',
        'msg': 'Unexpected error'
    }

    with pytest.raises(UnknownAPIException) as e:
        raise UnknownAPIException
    e = e.value

    assert e.status_code == 500
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())


def test_exception_external_api_exception():
    expected_result = {
        'code': 'external_api_error',
        'msg': 'test API is not working properly.'
    }

    with pytest.raises(ExternalAPIException) as e:
        raise ExternalAPIException(api_name='test API')
    e = e.value

    assert e.status_code == 503
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())


def test_exception_api_throttling_exception():
    expected_result = {
        'code': 'api_throttling',
        'msg': 'test API needs to cool down.'
    }

    with pytest.raises(APIThrottlingException) as e:
        raise APIThrottlingException(api_name='test API')
    e = e.value

    assert e.status_code == 429
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())


def test_exception_invalid_credentials_exception():
    expected_result = {
        'code': 'invalid_credentials',
        'msg': 'test API credentials are not valid.'
    }

    with pytest.raises(InvalidCredentialsException) as e:
        raise InvalidCredentialsException(api_name='test API')
    e = e.value

    assert e.status_code == 401
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())


def test_exception_operation_failed_exception():
    expected_result = {
        'code': 'operation_failed',
        'msg': 'API failed to process your request.'
    }

    with pytest.raises(OperationFailedException) as e:
        raise OperationFailedException
    e = e.value

    assert e.status_code == 422
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())


def test_exception_bad_parameter_exception():
    expected_result = {
        'code': 'bad_parameter',
        'msg': 'test is not correct.'
    }

    with pytest.raises(BadParameterException) as e:
        raise BadParameterException(parameter='test')
    e = e.value

    assert e.status_code == 400
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())

    expected_result = {
        'code': 'bad_parameter',
        'msg': 'test is not correct. Valid values are: test1, test2'
    }

    with pytest.raises(BadParameterException) as e:
        raise BadParameterException(parameter='test', valid_values=['test1', 'test2'])
    e = e.value

    assert e.status_code == 400
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())


def test_exception_missing_parameter_exception():
    expected_result = {
        'code': 'missing_parameter',
        'msg': 'test is missing.'
    }

    with pytest.raises(MissingParameterException) as e:
        raise MissingParameterException(parameter='test')
    e = e.value

    assert e.status_code == 400
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())


def test_exception_missing_header_exception():
    expected_result = {
        'code': 'missing_header',
        'msg': 'test is missing.'
    }

    with pytest.raises(MissingHeaderException) as e:
        raise MissingHeaderException(header='test')
    e = e.value

    assert e.status_code == 400
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())


def test_exception_bad_header_exception():
    expected_result = {
        'code': 'bad_header',
        'msg': 'test is not correct.'
    }

    with pytest.raises(BadHeaderException) as e:
        raise BadHeaderException(header='test')
    e = e.value

    assert e.status_code == 400
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())

    expected_result = {
        'code': 'bad_header',
        'msg': 'test is not correct. Valid values are: test1, test2'
    }

    with pytest.raises(BadHeaderException) as e:
        raise BadHeaderException(header='test', valid_values=['test1', 'test2'])
    e = e.value

    assert e.status_code == 400
    assert sorted(e.to_dict().items()) == sorted(expected_result.items())
