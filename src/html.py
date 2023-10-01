# src/html.py

import pycountry
from wrapper.zipcode import Zipcode
from wrapper.forecast import Forecast
from wrapper.parser import Parser
from wrapper.day import Day

from fastapi import FastAPI, HTTPException, status, Request, Response, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from starlette.background import BackgroundTask

DIRECTION = [
        "Please enter the requested Zip code",
        "",
        "By default, the zipcode entered checks against US zipcodes",
        "If you need a specific country's 5 days weather forecast, use: zip,XX format (i.e. 10004,US)",
        "Or, just use the country drop-down option",
        ""
        ]

FORM = 'form.html'

app = FastAPI()

templates = Jinja2Templates(directory='templates/')

country_list = [i.alpha_2 for i in pycountry.countries]
country_list_of_dict = [{'name': i.name, 'code': i.alpha_2} for i in pycountry.countries]
print(country_list_of_dict)
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
        result = response['message']

        return templates.TemplateResponse(FORM, context={'request': request, 'direction': DIRECTION, 'countries': country_list_of_dict, 'selected': selected,  'result': result, 'zip': zip})
    else:
        forecast_instance = Forecast(response['lat'], response['lon'])
        response = forecast_instance.result()
        if 'cod' in response and response['cod'] == '404': # cheking for response code (mainly for errors)
            result = response['message']

            return templates.TemplateResponse(FORM, context={'request': request, 'direction': DIRECTION, 'countries': country_list_of_dict, 'selected': selected,  'result': result, 'zip': zip})

        parser_instance = Parser(response)
        result = parser_instance.datadict()

    return templates.TemplateResponse(FORM, context={'request': request, 'direction': DIRECTION, 'countries': country_list_of_dict, 'selected': selected,  'result': result, 'zip': zip})