# src/html.py

import pycountry
from wrapper.zipcode import Zipcode
from wrapper.forecast import Forecast
from wrapper.parser import Parser

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

DIRECTION = [
        "Please enter the requested Zip code",
        "",
        "By default, the zipcode entered checks against US zipcodes",
        "If you need a specific country's 5 days weather forecast, use: zip,XX format (i.e. 10004,US)",
        "Or, just use the country drop-down option",
        "",
        "Note: openweathermap zip api does not support all countries",
        "Tested countries that openweathermap zip API does return lan,lot for: Great Britain, Unites States, Germany, Italy, Spain, France, Sweeden, Finland",
        "Tested countries that openweathermap zip API does not return lat,lon for: Brazil, Israel",
        ""
        ]

FORM = 'form.html'

app = FastAPI()

templates = Jinja2Templates(directory='templates/')

country_list = [i.alpha_2 for i in pycountry.countries]
country_list_of_dict = [{'name': i.name, 'code': i.alpha_2} for i in pycountry.countries]
country_list.sort()

@app.get('/')
def form_get(request: Request, selected: bool = False):
    result = ''
    return templates.TemplateResponse(FORM, context={'request': request, 'direction': DIRECTION, 'countries': country_list_of_dict, 'selected': selected, 'result': result})

@app.post('/')
def form_post(request: Request, zip: str = Form(None), selected: bool = False, country_codes: str = Form(None)):
    if selected is False:
        zip_instance = Zipcode(zip)
    else:
        zip_instance = Zipcode(zip, country_codes)
        print(zip, " ", country_codes)

    response = zip_instance.result()

    if 'cod' in response: # cheking for response code (mainly for errors)
        result = {'error': 'yes', 'code': response['cod'], 'message': response['message']}

        #return templates.TemplateResponse(FORM, context={'request': request, 'direction': DIRECTION, 'countries': country_list_of_dict, 'selected': selected,  'result': result, 'zip': zip})
    else:
        forecast_instance = Forecast(response['lat'], response['lon'])
        response = forecast_instance.result()
        if 'cod' in response: # cheking for response code (mainly for errors)
            result = {'error': 'yes', 'code': response['cod'], 'message': response['message']}

            #return templates.TemplateResponse(FORM, context={'request': request, 'direction': DIRECTION, 'countries': country_list_of_dict, 'selected': selected,  'result': result, 'zip': zip})

        parser_instance = Parser(response)
        result = parser_instance.datadict()

    return templates.TemplateResponse(FORM, context={'request': request, 'direction': DIRECTION, 'countries': country_list_of_dict, 'selected': selected,  'result': result, 'zip': zip})