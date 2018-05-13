class APIException(Exception):
    status_code = 500

    def __init__(self, code='api_error', msg='Unexpected error'):
        super().__init__(msg)
        self.code = code
        self.msg = msg

    def to_dict(self):
        return {
            'code': self.code,
            'msg': self.msg
        }


class ExternalAPIException(APIException):
    status_code = 503

    def __init__(self, api_name='External'):
        super().__init__(
            'external_api_error',
            '{} API is not working properly'.format(api_name)
        )


class APIThrottlingException(APIException):
    status_code = 429

    def __init__(self, api_name='External'):
        super().__init__(
            'api_throttling',
            '{} API is not working properly'.format(api_name)
        )


class InvalidCredentialsException(APIException):
    status_code = 401

    def __init__(self, api_name='External'):
        super().__init__(
            'invalid_credentials',
            '{} API credentials are not valid.'.format(api_name)
        )


class OperationFailedException(APIException):
    def __init__(self):
        super().__init__(
            'operation_failed',
            'API failed to process your request. Try again.'
        )


class MissingParameterException(APIException):
    status_code = 400

    def __init__(self, parameter):
        super().__init__(
            'missing_parameter',
            '{} is missing.'.format(parameter)
        )


class BadParameterException(APIException):
    status_code = 400

    def __init__(self, parameter, valid_values=None):
        msg = '{} is not correct.'.format(parameter)
        if valid_values:
            msg = msg + ' Valid values are {}'.format(', '.join(valid_values))
        super().__init__(
            'bad_parameter',
            msg
        )


class MissingHeaderException(APIException):
    status_code = 400

    def __init__(self, parameter):
        super().__init__(
            'missing_header',
            '{} is missing.'.format(parameter)
        )


class BadHeaderException(APIException):
    status_code = 400

    def __init__(self, parameter, valid_values=None):
        msg = '{} is not correct.'.format(parameter)
        if valid_values:
            msg = msg + ' Valid values are {}'.format(', '.join(valid_values))
        super().__init__(
            'bad_header',
            msg
        )
