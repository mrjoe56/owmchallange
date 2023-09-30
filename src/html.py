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

DIRECTION = 'Please enter the requested Zip code'

app = FastAPI()

templates = Jinja2Templates(directory='templates/')

country_list = [i.alpha_2 for i in pycountry.countries]
country_list.sort()

@app.get('/')
def form_post(request: Request):
    result = ''
    return templates.TemplateResponse('form.html', context={'request': request, 'direction': DIRECTION, 'countries': country_list, 'result': result})

@app.post('/')
def form_post(request: Request, zip: str = Form(None)):
    zip_instance = Zipcode(zip)
    response = zip_instance.result()

    #print(response)

    if 'cod' in response: # cheking for response code (mainly for errors)
        result = response['message']

        print("result = ", result)

        return templates.TemplateResponse('form.html', context={'request': request, 'direction': DIRECTION, 'countries': country_list, 'result': result, 'zip': zip})
    else:
        forecast_instance = Forecast(response['lat'], response['lon'])
        response = forecast_instance.result()
        if 'cod' in response and response['cod'] == '404': # cheking for response code (mainly for errors)
            result = response['message']

            print("result = ", result)

            return templates.TemplateResponse('form.html', context={'request': request, 'direction': DIRECTION, 'countries': country_list, 'result': result, 'zip': zip})

        parser_instance = Parser(response)
        result = parser_instance.datadict()
    
    print("result = ", result)

    return templates.TemplateResponse('form.html', context={'request': request, 'direction': DIRECTION, 'countries': country_list, 'result': result, 'zip': zip})