# -*- coding: utf-8 -*-
"""
** Affective IT for SuriRobot
** 
** Made by Alexandre Brun
** Login   <alexandre.brun@suricats-consulting.com>
** 
** Started on  Wed Oct 17 10:51:11 2017 Alexandre Brun
"""

import requests
import json
"""
Méthode pour call l'API Beyond Verbal et soumettre un extrait sonore à étude.
1er param: clé API
2e  param : Path de l'extrait audio
"""
def getAnalysis(API_Key,WavPath):

    res = requests.post("https://token.beyondverbal.com/token",data={"grant_type":"client_credentials","apiKey":API_Key})
    token = res.json()['access_token']
    headers={"Authorization":"Bearer "+token}

    pp = requests.post("https://apiv4.beyondverbal.com/v4/recording/start",json={"dataFormat": { "type":"WAV" }},verify=False,headers=headers)
    if pp.status_code != 200:
        print(pp.status_code, pp.content)
        return
    recordingId = pp.json()['recordingId']
    with open(WavPath,'rb') as wavdata:
        r = requests.post("https://apiv4.beyondverbal.com/v4/recording/"+recordingId,data=wavdata, verify=False, headers=headers)
        return r.json()


data = getAnalysis("755df2e5-10d6-41d1-8f12-3e1b34325261","samples/collectif_fr.wav")
print(json.dumps(data, sort_keys=True, indent=4))
