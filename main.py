import urllib.request
import json

APIKey = "714c2da2279a72ec8bb713798409d352"

city_name = input("Search for a city by name: ")
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s" % (city_name, APIKey)

req = urllib.request.urlopen(url).read().decode()
data = json.loads(req)

print("City: %s\nWeather: %s\nTemperature: %s°F" % (data["name"], data["weather"][0]["main"], round((data["main"]["temp"] - 273.15) * 9/5 + 32, 2)))