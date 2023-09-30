# wrapper/forecast.py

#from . import session

import requests
session = requests.Session()
session.params = {}
session.params['appid'] = ''

class FORECAST(object): # object's constructor initialised by the lattitude and the longtitude
  def __init__(self, lat: float, lon: float):
    self.lat = lat
    self.lon = lon
  
  def result(self): # returns the APIs results
    path = 'http://api.openweathermap.org/data/2.5/forecast'
    session.params['lat'] = self.lat
    session.params['lon'] = self.lon
    session.params['units'] = 'metric'
    response = session.get(path)
    return response.json() # which is a list of 5 days forcast seperated by 3 hours (owm free account)