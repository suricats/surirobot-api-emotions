import requests
import json
import certifi
import urllib3

from api.exceptions import ExternalAPIException, InvalidCredentialsException, APIThrottlingException, OperationFailedException, TokenExpiredOrInvalidException
from api.beyond_verbal.constants import BEYONDVERBAL_API_KEY, BEYONDVERBAL_API_URL, BEYONDVERBAL_TOKEN_URL
from ffmpy import FFmpeg

API_NAME = 'Beyond Verbal API'

"""
Méthode pour call l'API Beyond Verbal et soumettre un extrait sonore à étude.
1er param: Path de l'extrait audio
"""
def beyond_verbal_analyse_voice(file):

    """
        http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    """
    requests.packages.urllib3.disable_warnings()

    res = requests.post(BEYONDVERBAL_TOKEN_URL,data={"grant_type":"client_credentials","apiKey":BEYONDVERBAL_API_KEY})
    token = res.json()['access_token']
    headers={"Authorization":"Bearer "+token}

    pp = requests.post(BEYONDVERBAL_API_URL + "/recording/start",json={"dataFormat": { "type":"WAV" }},verify=False,headers=headers)
    if pp.status_code == 200:
        recordingId = pp.json()['recordingId']
        new_file = file.split('.')[0] + '-format.wav'
        ff = FFmpeg(
            inputs={file: None},
            outputs={new_file: '-acodec pcm_s16le -ac 1 -ar 8000'}
        )
        ff.run()

        with open(new_file, 'rb') as wavdata:
            r = requests.post(BEYONDVERBAL_API_URL + "/recording/"+recordingId,data=wavdata, verify=False, headers=headers)
        
        print (json.dumps(r.json(), indent=4, sort_keys=True))
        return r.json()
    elif pp.status_code == 401:
        raise InvalidCredentialsException(api_name='Beyond Verbal')
    elif pp.status_code == 429:
        raise APIThrottlingException(api_name='Beyond Verbal')
    elif pp.status_code == 498:
        raise TokenExpiredOrInvalidException(code='Beyond Verbal', msg=pp.text)

    else:
        print(res.status_code + res.text)
        raise ExternalAPIException(api_name=res.status_code)

"""

res = requests.post("https://token.beyondverbal.com/token", data={"grant_type": "client_credentials",
                                                                          "apiKey": os.environ.get('BEYONDVERBAL_API_CREDENTIAL')})
        token = res.json()['access_token']
        headers = {"Authorization": "Bearer "+token}

        pp = requests.post("https://apiv4.beyondverbal.com/v4/recording/start",
                           json={"dataFormat": {"type": "WAV"}},
                           verify=False,
                           headers=headers)
        if pp.status_code != 200:
            self.logger.error('HTTP {} error occurred.'.format(pp.status_code))
            self.signal_indicator.emit("emotion", "red")
            return
        else : 
            recordingId = pp.json()['recordingId']
            new_file = file_path.split('.')[0] + '-format.wav'
            ff = FFmpeg(
                inputs={file_path: None},
                outputs={new_file: '-acodec pcm_s16le -ac 1 -ar 8000'}
            )
            ff.run()

            with open(new_file, 'rb') as wavdata:
                r = requests.post("https://apiv4.beyondverbal.com/v4/recording/"+recordingId,
                              data=wavdata,
                              verify=False,
                              headers=headers)
               # parsed = json.loads(r.json())
                print (json.dumps(r.json(), indent=4, sort_keys=True))
                return r.json()
"""
        #data = getAnalysis(BEYONDVERBAL_API_CREDENTIAL, "samples/output.wav")
        #print(json.dumps(data, sort_keys=True, indent=4))