from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.gis.geoip2 import GeoIP2
from django.contrib import messages
from .forms import CityForm

import requests
import os


current_location_weather = None
other_location_weather = None


def index(request):

	global display, current_location_weather, other_location_weather

	# Using GeoIP2 to get user's current location based on user IP address
	if current_location_weather == None:	
		g = GeoIP2()
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')

		try:
			current_location = g.city(ip)['city']
			current_location_weather = get_weather(request, current_location)
		except:
			current_location_weather = None	
	
	# Handle user input for other location
	if request.method == 'POST':
		form = CityForm(request.POST)

		if form.is_valid():
			city = form.cleaned_data['city'].lower()
			other_location_weather = get_weather(request, city)
			return HttpResponseRedirect('/')		 
	
	else:
		form = CityForm()

	context = {
		'current_location_weather': current_location_weather,
		'other_location_weather': other_location_weather,
		'form': form,
		# 'display': display
	}
	
	return render(request, 'weather/index.html', context)


# Making an API request to get the current weather
def get_weather(request, city):
	
	base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={os.environ['API_KEY']}"
	response = requests.get(base_url)

	if response:
		data = response.json()
		weather= {
			'city': data['name'],
			'country': data['sys']['country'],
			'temperature': data['main']['temp'],
			'description': data['weather'][0]['description'].capitalize(),
			'icon': data['weather'][0]['icon']
		}
		return weather				

	else:
		messages.error(request, 'No results!')
		return None