import requests
import json
from pprint import pprint
#test url: https://thebluealliance.com/api/v2/ ?X-TBA-App-Id=frc2849:SmileMonster:vTestLink

def get_team_bio(teamkey):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/team/%s' % teamkey
    data = requests.get(url, params=urlPARAM)
    json = data.json()
    return json
