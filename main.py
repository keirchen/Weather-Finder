"""
Keira Chen
Weather Finder code-your-own project
This was made partially following a Replit tutorial for using web APIs
(Not defensive)
"""

import urllib.request
import json

#api key
APIKey = "714c2da2279a72ec8bb713798409d352"

#prompts user to search for a city
city_name = input("Search for a city by name: ")
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s" % (city_name, APIKey)

#grabs data
req = urllib.request.urlopen(url).read().decode()
data = json.loads(req)

#prints results: the city, the weather status, the temperature in fahrenheit
print("City: %s\nWeather: %s\nTemperature: %s°F" % (data["name"], data["weather"][0]["main"], round((data["main"]["temp"] - 273.15) * 9/5 + 32, 2)))