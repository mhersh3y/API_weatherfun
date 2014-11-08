# had to do this SUDO install
# source venv/bin/activate
# pip freeze - makes sure you are in the venv

import requests
from pprint import pprint
import random


# r = requests.get('http://api.wunderground.com/api/db2b844797b8ee66/conditions/q/CA/San_Francisco.json')

# print r.status_code
# print r.json()

# j = r.json()
# pprint(j)

# temperature = j['current_observation']['temperature_string']
# state = j['current_observation']['display_location']['state']
# city = j['current_observation']['display_location']['city']


# def weather():
# 	#returns weather
# 	print temperature
# 	print city
# 	print state

#################################
# How I did it
#
######################################

# def weather(state,city):
# 	city = city.replace(" ", "_")
# 	concatenate = 'http://api.wunderground.com/api/db2b844797b8ee66/conditions/q/' + state + '/' + city + '.json'
# 	# print concatenate
# 	r =requests.get(concatenate)
# 	# print r.status_code
# 	j = r.json()
# 	# pprint(j)
# 	called_temp =j['current_observation']['temperature_string']
# 	print called_temp

# weather('CA','San Francisco') 


#################################
# How Hackbright does it
#
#################################
# BASE_URL = 'http://api.wunderground.com/api/YOUR_API_KEY_GOES_HERE/conditions/q/'

# def get_api_url(state, city):
#     city = city.replace(" ", "_")
#     return "{}/{}/{}".format(BASE_URL, state, city)
    
# # test
# print get_api_url("CA", "San Francisco")
# print get_api_url("NY", "New York")



#################################
# How I did it
#
######################################

BASE_URL = 'http://api.wunderground.com/api/db2b844797b8ee66/forecast/q'
# r = requests.get('http://api.wunderground.com/api/db2b844797b8ee66/forecast/q/CA/San_Francisco.json')

# print r.status_code
# print r.json()

# j = r.json()

# forecasting = j['forecast']['simpleforecast']['forecastday']['date']['weekday'] list mode

def get_api_url(state, city):
    city = city.replace(" ", "_")
    return "{}/{}/{}.json".format(BASE_URL, state, city)

def forecast(state,city):
	string = get_api_url(state,city)
	r = requests.get(string)
	j = r.json()
	forecasting2 = j['forecast']['txt_forecast']['forecastday']
	for i in forecasting2:
		# print i
		day = i['title']
		forecast = i['fcttext']
		# conditions = i['fcttext']
		print day
		print "   "
		print forecast
		print "-------------------"
		# print conditions

# pprint(j)#what if i wanted to look at only one of the dictionaries

# forecast('CA','San Francisco') 

source_places = [ ('New York', 'NY'), ('San Francisco', 'CA'), ('Seattle', 'WA'), ('Houston', 'TX') ]
ny = source_places[0]
# print random.choice(source_places)



def get_random_place_name():
	location = random.choice(source_places)
	state = location[0] 
	city = location[1]
	return state,city




(city,state) = get_random_place_name()

get_random_place_name()

print (city,state)


