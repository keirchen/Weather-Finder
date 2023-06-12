import urllib.request
import json

APIKey = "714c2da2279a72ec8bb713798409d352"

cityName = input("City name: ")
cityName = cityName.lower()
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s" % (cityName, APIKey)