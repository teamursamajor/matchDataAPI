import urllib.request
import json
import pprint

URL = 'https://www.thebluealliance.com/api/v2/'
HEADER_KEY = '?X-TBA-App-Id='
HEADER_VAL = 'frc2849:scouting-machine:v01'

# returns a list of the teams (FRCXXXX) participating in an event
def get_event_teams(event_key):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	#request = urllib.request.Request(URL + 'event/' + event_key + '/teams', HEADER_KEY, HEADER_VAL)
	response =
	jsonified = json.loads(response.read().decode("utf-8"))
	teams = []

	for team in jsonified:
		teams.append(team['key'])

	return teams



print (get_event_teams('2010sc'))
