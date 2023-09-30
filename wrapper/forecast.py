# wrapper/forecast.py

from dotenv import load_dotenv
import os
import requests

class Forecast(object): # object's constructor initialised by the lattitude and the longtitude
  def __init__(self, lat: float, lon: float):
    self.appid = os.getenv('OWM_API_KEY')
    self.lat = lat
    self.lon = lon
    self.UNITS = 'metric'
  
  def result(self): # returns the APIs results
    path = 'http://api.openweathermap.org/data/2.5/forecast'

    # api 2.5 works with session, so a session needed to be created
    self.session = requests.Session()
    self.session.params = {}
    self.session.params['lat'] = self.lat
    self.session.params['lon'] = self.lon
    self.session.params['units'] = self.UNITS
    self.session.params['appid'] = self.appid

    response = self.session.get(path)

    # api 3.0 doesn't need a session, it's much better (but, I'm working with 2.5)
    #response = requests.get(path, params = {'lat': self.lat, 'lon': self.lon, 'units': self.UNITS})

    return response.json() # which is a list of 5 days forcast seperated by 3 hours (owm free account)