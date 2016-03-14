import requests
import json
from pprint import pprint

def get_event_teams(event_key, team_key):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = ('https://thebluealliance.com/api/v2/team/%s/event/%s/matches' %(team_key,event_key))
    print (url)
    data = requests.get(url, params=urlPARAM)
    json = data.json()
    return json
    
pprint (get_event_teams('2016mdbet', 'frc2849'))

