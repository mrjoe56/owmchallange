# wrapper/zipcode.py

from dotenv import load_dotenv
import os
import requests

class Zipcode(object): # object's constructor initialised by the zip code
  def __init__(self, zip_code, country: str = None) -> None:
    load_dotenv()
    self.appid = os.getenv('OWM_API_KEY')
    self.zip_code = zip_code
    self.country = country

  def result(self): # returns the APIs results
    path = 'http://api.openweathermap.org/geo/1.0/zip'

    # api 2.5 works with session, so a session needed to be created
    self.session = requests.Session()
    self.session.params = {}

    if self.country is not None: # condition based on if country code drop-down was selected
      self.session.params['zip'] = self.zip_code + "," + self.country # set the zip query
    else:
      self.session.params['zip'] = self.zip_code # if drop-down wasn't selected, then, take the zip from the form field as is

    self.session.params['appid'] = self.appid # add the key in the request

    response = self.session.get(path)
    print(response.request.url)

    # api 3.0 doesn't need a session, it's much better (but, I'm working with 2.5) / if I'll have time, I'll build it for 3.0 as well, and I'll put them side-by-side
    #response = self.session.get(path, params = {'zip': self.zip_code, 'appid': self.appid})
    
    return response.json() # which also includes the altitude and longtitude