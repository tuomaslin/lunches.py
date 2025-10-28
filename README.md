# Small project to search for lunch menus near to given street or place
The script uses [lounaat.info](https://lounaat.info) to search for restaurants and their lunch menus.

## How to use
If you don't have all libraries used in the script run ```pip3 install -r requirements.txt```

Run ```~$ python3 lunches.py lauttasaari```, where _lauttasaari_ is the place where you would like to find restaurants from.

_Optional_ run the script in a virtual environment with
	1. ```~$ virtualenv venv```
	2. ```~$ source venv/bin/activate```
	3. ```~$ pip3 install -r requirements.txt```
	4. ```~$ python3 lunches.py lauttasaari```