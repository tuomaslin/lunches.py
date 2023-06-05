#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.lounaat.info/ajax/filter?'
params = {
        'view':'suosikit',
        'day':datetime.now().weekday()+1,
        'page':'0',
        'coords[lat]':'60.17971599562645',
        'coords[lng]':'24.83791189049072',
        'coords[address]':'keilaniemi-espoo',
        'coords[formattedAddress]':'Keilaniemi, Espoo'
}

headers = {
        'Referer':'https://www.lounaat.info/',
}

cookies = {
	'favs_v2':'[2194,2782,2788,3985,4361,4614]'
}

r = requests.get(url, params=params, headers=headers, cookies=cookies)
soup = BeautifulSoup(r.text, 'html.parser')

print('\n')
for x in soup:
        print('[!]',x.h3.text.upper(),'\n','-'*30)
        l = x.find_all('p', {'class':'dish'})
        for i in l:
                print(i.text)
        print('\n')
