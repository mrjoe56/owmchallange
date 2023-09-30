# wrapper/zipcode.py

from dotenv import load_dotenv
import os
import requests

class Zipcode(object): # object's constructor initialised by the zip code
  def __init__(self, zip_code) -> None:
    load_dotenv()
    self.appid = os.getenv('OWM_API_KEY')
    self.zip_code = zip_code

  def result(self): # returns the APIs results
    path = 'http://api.openweathermap.org/geo/1.0/zip'

    # api 2.5 works with session, so a session needed to be created
    self.session = requests.Session()
    self.session.params = {}
    self.session.params['zip'] = self.zip_code
    self.session.params['appid'] = self.appid

    response = self.session.get(path)

    # api 3.0 doesn't need a session, it's much better (but, I'm working with 2.5)
    #response = self.session.get(path, params = {'zip': self.zip_code, 'appid': self.appid})
    
    return response.json() # which also includes the altitude and longtitude