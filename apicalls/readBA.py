import requests
import json
from pprint import pprint
#test url: https://thebluealliance.com/api/v2/ ?X-TBA-App-Id=frc2849:SmileMonster:vTestLink

def get_event_teams(event_key):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/event/%s/teams' % event_key
    data = requests.get(url, params=urlPARAM)
    json = data.json()
    return json

def test_case(event_key):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/event/%s' % event_key
    data = requests.get(url, params=urlPARAM)
    json = data.json()
    return json

def get_team_stats(teamkey): #under development
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/event/%s/teams' % teamkey
    data = requests.get(url, params=urlPARAM)
    json = data.json()
    return json

def get_team_bio(teamkey):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/team/%s' % teamkey
    data = requests.get(url, params=urlPARAM)
    json = data.json()
    return json

def get_event_teams(event_key):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/event/%s/teams' % event_key
    data = requests.get(url, params=urlPARAM)
    json = data.json()
    return json

def get_event_matches(event_key):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/event/%s/matches' % event_key
    data = requests.get(url, params=urlPARAM)
    json = data.json()
    return json
