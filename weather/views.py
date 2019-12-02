from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2


def index(request):

	# Using GeoIP2 to get user's current location based on user IP address
	g = GeoIP2()

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')

	try: current_location = g.city(ip)['city']
	except: current_location = None	
	
	context = {
		'current_location': current_location,
	}

	return render(request, 'weather/index.html', context)