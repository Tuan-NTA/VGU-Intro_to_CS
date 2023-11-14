import datetime as dt
import requests

class Weather:
    def __init__(self, api_key: str, city: str, scheduler, chat_botapp):
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        self.API_KEY = api_key
        self.CITY = city
        self.scheduler = scheduler 
        self.chat_botapp = chat_botapp  # Corrected attribute name
        self.get_weather()

    def kelvin_to_celsius_fahrenheit(self, kelvin: float) -> tuple:
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

    def get_weather(self):
        url = self.BASE_URL + "appid=" + self.API_KEY + "&q=" + self.CITY
        response = requests.get(url).json()

        self.temp_kelvin = response['main']['temp']
        self.temp_celsius, self.temp_fahrenheit = self.kelvin_to_celsius_fahrenheit(self.temp_kelvin)
        self.feels_like_kelvin = response['main']['feels_like']
        self.feels_like_celsius, self.feels_like_fahrenheit = self.kelvin_to_celsius_fahrenheit(self.feels_like_kelvin)
        self.wind_speed = response['wind']['speed']
        self.humidity = response['main']['humidity']
        self.description = response['weather'][0]['description']

        
  

    def Weather_run(self):
        self.get_weather() 
        if self.scheduler.shared_data[0] == "Retrieving weather data":
            self.chat_botapp.Insert_response(f"Temperature in {self.CITY}: {self.temp_celsius:.2f}C or {self.temp_fahrenheit:.2f}F"+
                                             f"\nTemperature in {self.CITY} feels like: {self.feels_like_celsius:.2f}C or {self.feels_like_fahrenheit:.2f}F"+
                                             f"\nHumidity in {self.CITY}: {self.humidity}%"
                                             +f"\nWind speed in {self.CITY}: {self.wind_speed}m/s"
                                             +f"\nGeneral weather in {self.CITY}: {self.description}")            
                
            self.scheduler.shared_data[0] = ""



