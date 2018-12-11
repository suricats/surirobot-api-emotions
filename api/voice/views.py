import requests
import json
from ffmpy import FFmpeg
import os



def save_results(self, r, image_id, user_id=None):
        if user_id is not None:
            with open(self.TMP_DIR + '{}-emotion-{}.json'.format(user_id, image_id), 'w') as outfile:
                json.dump(r.json(), outfile)

@ehpyqtSlot(str, str, int)
@ehpyqtSlot(str)
def getAnalysis(self, file_path, image_id=None, user_id=None):

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
    else:
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
            self.save_results(r, image_id, user_id)
            return r.json()

    #data = getAnalysis(BEYONDVERBAL_API_CREDENTIAL, "samples/output.wav")
    #print(json.dumps(data, sort_keys=True, indent=4))