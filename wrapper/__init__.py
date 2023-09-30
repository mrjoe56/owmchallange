import os
import requests

OWM_API_KEY = os.environ.get('OWM_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if OWM_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. "
        "See https://openweathermap.org/api for how to retrieve an auth token from the Open Weather Map"
    )

session = requests.Session()
session.params = {}
session.params['appid'] = OWM_API_KEY

from .zipcode import ZIPCODE