import requests
import json
from pprint import pprint
from readBA import *

def main():
	print ("Welcome to 2849's TBA reader:\n Enter the number for what you are interested in:\n1. Team Stats\n2. Team Bio\n3. Event Stat\n4. Event Bio")
    userSelection = input()
    if (userSelection == str(1)):
        key = input('Enter the team number:')
        pprint (get_team_stats('frc', key))
    if (userSelection == str(2)):
        key = 'frc%s' % input('Enter the team number:')
        pprint (get_team_bio(key))
