class BaseAPIException(Exception):
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


class UnknownAPIException(BaseAPIException):
    status_code = 500

    def __init__(self):
        super().__init__()


class ExternalAPIException(BaseAPIException):
    status_code = 503

    def __init__(self, api_name='External API'):
        super().__init__(
            'external_api_error',
            '{} is not working properly.'.format(api_name)
        )


class APIThrottlingException(BaseAPIException):
    status_code = 429

    def __init__(self, api_name='External API'):
        super().__init__(
            'api_throttling',
            '{} needs to cool down.'.format(api_name)
        )


class InvalidCredentialsException(BaseAPIException):
    status_code = 401

    def __init__(self, api_name='External API'):
        super().__init__(
            'invalid_credentials',
            '{} credentials are not valid.'.format(api_name)
        )


class OperationFailedException(BaseAPIException):
    status_code = 422

    def __init__(self):
        super().__init__(
            'operation_failed',
            'API failed to process your request.'
        )


class MissingParameterException(BaseAPIException):
    status_code = 400

    def __init__(self, parameter):
        super().__init__(
            'missing_parameter',
            '{} is missing.'.format(parameter)
        )


class BadParameterException(BaseAPIException):
    status_code = 400

    def __init__(self, parameter, valid_values=None):
        msg = '{} is not correct.'.format(parameter)
        if valid_values:
            msg = msg + ' Valid values are: {}'.format(', '.join(valid_values))
        super().__init__(
            'bad_parameter',
            msg
        )


class MissingHeaderException(BaseAPIException):
    status_code = 400

    def __init__(self, header):
        super().__init__(
            'missing_header',
            '{} is missing.'.format(header)
        )


class BadHeaderException(BaseAPIException):
    status_code = 400

    def __init__(self, header, valid_values=None):
        msg = '{} is not correct.'.format(header)
        if valid_values:
            msg = msg + ' Valid values are: {}'.format(', '.join(valid_values))
        super().__init__(
            'bad_header',
            msg
        )
class TokenExpiredOrInvalidException(BaseAPIException):
    status_code = 498

    def __init__(self, code='498', msg='Unexpected error'):
        super().__init__(
            code,
            msg
        )
