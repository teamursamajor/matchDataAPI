import requests
import json
from pprint import pprint
#test url: https://thebluealliance.com/api/v2/ ?X-TBA-App-Id=frc2849:SmileMonster:vTestLink

def test_case(event_key):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/event/%s' % event_key
    data = requests.get(url, params=urlPARAM)
    json = data.json()
    return json

