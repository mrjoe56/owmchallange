# src/html.py

from wrapper.zipcode import ZIPCODE
from wrapper.forecast import FORECAST
from wrapper.parser import PARSER
from wrapper.day import DAY

from fastapi import FastAPI, HTTPException, status, Request, Response, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
from starlette.background import BackgroundTask
from http import HTTPStatus
import uvicorn

DIRECTION = 'Please enter the requested Zip code'

app = FastAPI()

templates = Jinja2Templates(directory='templates/')

@app.get('/')
def form_post(request: Request):
    result = ''
    return templates.TemplateResponse('form.html', context={'request': request, 'direction': DIRECTION, 'result': result})

@app.post('/')
def form_post(request: Request, zip: str = Form(...)):
    zip_instance = ZIPCODE(zip)
    response = zip_instance.result()

    print(response)

    if 'cod' in response:
        result = response['message']
        return templates.TemplateResponse('error.html', context={'request': request, 'direction': DIRECTION, 'result': result, 'zip': zip})
    else:
        forecast_instance = FORECAST(response['lat'], response['lon'])
        response = forecast_instance.result()
        if 'cod' in response and response['cod'] == '404':
            result = response['message']
            return templates.TemplateResponse('error.html', context={'request': request, 'direction': DIRECTION, 'result': result, 'zip': zip})

        parser_instance = PARSER(response)
        result = parser_instance.datalist()
    
    return templates.TemplateResponse('form.html', context={'request': request, 'direction': DIRECTION, 'result': result, 'zip': zip})