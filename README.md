# WeatherApp

A django based web application that provides weather details about the user enered location based on **OpenWeatherMapAPI**.

> Steps to follow
1. Install **pipenv** using the command \
 	`pip install pipenv`

2.  Clone the repo and run the following command to install all the dependencies \
	`pipenv install`

3.	Create an account on [OpenWeatherMap](https://openweathermap.org/) to generate an API key.

4. Create `.env` file in project root and add the following \
	`API_KEY = 'YOUR_API_KEY'`

5. Run the command from project root to start the project \
	`pipenv run python manage.py runserver` 


---
This project uses GeoLite2 data by MaxMind for retrieving user's current location, available [here]("https://www.maxmind.com") .