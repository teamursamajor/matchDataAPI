import urllib.request
import json
import pprint


URL = 'http://www.thebluealliance.com/api/v2/'
HEADER_KEY = 'X-TBA-App-Id'
HEADER_VAL = 'frc2849:scouting-machine:1'


# returns a list of the teams (team key) participating in an event
def get_event_teams(event_key):
	request = urllib.request.Request(URL + 'event/' + event_key + '/teams')
	request.add_header(HEADER_KEY, HEADER_VAL)
	response = urllib.request.urlopen(request)
	jsonified = json.loads(response.read().decode("utf-8"))
	teams = []

	for team in jsonified:
		teams.append(team['key'])

	return teams

def main():
    print get_event_teams('2010sc')
