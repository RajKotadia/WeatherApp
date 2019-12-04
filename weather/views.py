from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2

from django.http import HttpResponseRedirect
from .forms import CityForm

from django.contrib import messages


display = False
city = None


def index(request):

	global display, city

	# Using GeoIP2 to get user's current location based on user IP address
	g = GeoIP2()

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')

	try: current_location = g.city(ip)['city']
	except: current_location = None	
	
	# Handle user input for other location
	if request.method == 'POST':
		form = CityForm(request.POST)

		if form.is_valid():
			city = form.cleaned_data['city'].lower()

			# Make an API Request
			if city == 'mumbai':
				display = True
				
			else:
				display = False	
				messages.error(request, 'City does not exist!')

			return HttpResponseRedirect('/')		 
	
	else:
		form = CityForm()

	context = {
		'current_location': current_location,
		'other_city': city,
		'form': form,
		'display': display
	}
	
	return render(request, 'weather/index.html', context)