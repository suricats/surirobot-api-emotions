import requests

from api.exceptions import ExternalAPIException, InvalidCredentialsException, APIThrottlingException, OperationFailedException
from api.microsoft.constants import MICROSOFT_API_KEY, MICROSOFT_API_URL

API_NAME = 'Microsoft Face API'


def microsoft_analyse_picture(file):
    url = MICROSOFT_API_URL + '/detect?returnFaceId=true&returnFaceAttributes=emotion'
    params = {
        'returnFaceId': True,
        'returnFaceAttributes': ['emotion']
    }

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': MICROSOFT_API_KEY
    }

    res = requests.post(url=url, data=file, headers=headers, params=params)

    if res.status_code == 200:
        data = res.json()
        try:
            emotions = data[0]['faceAttributes']['emotion']
        except KeyError as e:
            raise OperationFailedException() from e

        if not emotions:
            raise OperationFailedException()

        emo = ''
        max_percent = 0
        for key, percent in emotions.items():
            if percent > max_percent:
                emo = key
                max_percent = percent

        return {
            'emotion': emo,
            'percent': max_percent
        }
    elif res.status_code == 401:
        raise InvalidCredentialsException(api_name='Microsoft')
    elif res.status_code == 429:
        raise APIThrottlingException(api_name='Microsoft')
    else:
        raise ExternalAPIException(api_name='Microsoft')
