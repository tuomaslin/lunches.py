#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from geopy.geocoders import Nominatim
import sys
from deep_translator import MyMemoryTranslator

def translate_text(text, target_language):
    try:
        translation = MyMemoryTranslator(source='finnish', target=target_language).translate(text)
    except:
        translation = text  # If translation fails, just use the original text
    return translation

try:
    place = sys.argv[1]
    target_language = sys.argv[2] if len(sys.argv) > 2 else 'english'  # use the second argument for target language, if provided

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
                    # Translate the dish
                    translation = translate_text(i.text, target_language)
                    print(f"{i.text} (translated: {translation})")
            print('\n')

except IndexError as err:
    print("Give address as an argument")
except AttributeError as err2:
    print("No restaurants found for given location")
