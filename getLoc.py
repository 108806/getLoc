#!/usr/bin/env python3
import json
import requests
import urllib
import argparse
import matplotlib as plt
from gcmap import GCMapper
gcm=GCMapper()

parser = argparse.ArgumentParser()

parser.add_argument("-target", "-t",
	help="Target IP to be searched for geolocation",
	default='8.8.8.8',
	)

parser.add_argument("--verbosity", "-v",
	help="""Level of intel displayed, 
	1 - only geolocation, 
	2 - geo + Country,
	3 - Everything.""",
	default=2,
	choices=[1,2,3],
	type=int
	)

args = parser.parse_args()


def getLoc(IP:str='8.8.8.8', verbosity=2):

	_GEO = 'http://geolocation-db.com/json/' + IP
	r = requests.get(_GEO, verify=False)
	try :
		res = json.loads(r.content.decode('utf8'))
	except : 
		print("Something is not yes...")
		sys.exit()
	simple = F"LAT : {res['latitude']} LON : {res['longitude']}"
	if verbosity==1 : return {simple} # Squares avoids splitting str by print*
	simple2 = F"Country : {res['country_name']} Code : {res['country_code']}"
	if verbosity==2 : return simple, simple2
	if verbosity==3 : return [x+" : "+str(res[x]) for x in res]

print(*getLoc(args.target, args.verbosity), sep='\n')