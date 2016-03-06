import requests
import json
from pprint import pprint


def get_event_teams(event_key):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/event/%s/teams' % event_key
    data = requests.get(url, params=urlPARAM)
    jsonofabitch = data.json()
    return jsonofabitch


def get_team_stats(teamkey):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/event/%s/teams' % event_key
    data = requests.get(url, params=urlPARAM)
    jsonofabitch = data.json()
    return jsonofabitch

def get_event_matches(event_key):
    urlPARAM = {'X-TBA-App-Id': 'frc2849:scouting-machine:v01'}
    url = 'https://thebluealliance.com/api/v2/event/%s/matches' % event_key
    data = requests.get(url, params=urlPARAM)
    jsonofabitch = data.json()
    return jsonofabitch

def main():
    pprint (get_event_matches('2016vahay'))
    #pprint (get_team_stats('frc2849'))
    #pprint (get_event_teams('2016vahay'))

main()
