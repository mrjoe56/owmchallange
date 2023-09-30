# wrapper/zipcode.py

from . import session

class ZIPCODE(object): # object's constructor initialised by the zip code
  def __init__(self, zipcode):
    self.zipcode = zipcode

  def result(self): # returns the APIs results
    path = 'http://api.openweathermap.org/geo/1.0/zip'
    session.params['zip'] = self.zipcode
    response = session.get(path)
    return response.json() # which also includes the altitude and longtitude