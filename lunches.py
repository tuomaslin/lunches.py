#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from geopy.geocoders import Nominatim
import sys


try:
	place = sys.argv[1]
	if place != "":

		geolocator = Nominatim(user_agent="MyApp")
		location = geolocator.geocode(place)

		url = 'https://www.lounaat.info/ajax/filter?'
		params = {
	        	'view':'lahella',
		        'day':datetime.now().weekday()+1,
		        'page':'0',
		        'coords[lat]':str(location.latitude),
		        'coords[lng]':str(location.longitude),
		}

		headers = {
		        'Referer':'https://www.lounaat.info/',
		}

		r = requests.get(url, params=params, headers=headers)
		soup = BeautifulSoup(r.text, 'html.parser')

		print('\n')
		for x in soup:
		        print('[!]',x.h3.text.upper(),'\n','-'*30)
		        l = x.find_all('p', {'class':'dish'})
		        for i in l:
		                print(i.text)
		        print('\n')

except IndexError as err:
	print("Give address as an argument")
except AttributeError as err2:
	print("No restaurants found for given location")
