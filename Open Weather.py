import datetime as dt
import requests

class Weather:
    def __init__(self, api_key: str, city: str):
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        self.API_KEY = api_key
        self.CITY = city

    def kelvin_to_celsius_fahrenheit(self, kelvin: float) -> tuple:
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

    def get_weather(self):
        url = self.BASE_URL + "appid=" + self.API_KEY + "&q=" + self.CITY
        response = requests.get(url).json()

        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = self.kelvin_to_celsius_fahrenheit(temp_kelvin)
        feels_like_kelvin = response['main']['feels_like']
        feels_like_celsius, feels_like_fahrenheit = self.kelvin_to_celsius_fahrenheit(feels_like_kelvin)
        wind_speed = response['wind']['speed']
        humidity = response['main']['humidity']
        description = response['weather'][0]['description']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

        print(f"Temperature in {self.CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
        print(f"Temperature in {self.CITY} feels like: {feels_like_celsius:.2f}°C or { feels_like_fahrenheit:.2f}°F")
        print(f"Humidity in {self.CITY}: {humidity}%")
        print(f"Wind speed in {self.CITY}: {wind_speed}m/s")
        print(f"General weather in {self.CITY}: {description}")
        print(f"Sunrise in {self.CITY} at {sunrise_time} local time")
        print(f"Sunset in {self.CITY} at {sunset_time} local time")

api_key = "Your_API_KEY"
city = input("Enter city name: ")
weather = Weather(api_key, city)
weather.get_weather()
