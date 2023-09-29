from fastapi import FastAPI, HTTPException, status,Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from wrapper.zip import ZIP
from wrapper.forecast import FORECAST
from wrapper.parser import PARSER
from wrapper.day import DAY


# ### working with JSON at the moment ###
# import json
# f = open('test.json')
# data = json.load(f)
# parser_instance = PARSER(data)
# ### working with JSON at the moment ###

DIRECTION = 'Please enter the requested Zip code'

app = FastAPI()
templates = Jinja2Templates(directory='templates/')

def save_to_text(content, filename):
    filepath = 'data/{}.txt'.format(filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath

@app.get('/')
def form_post(request: Request):
    result = ''
    return templates.TemplateResponse('form.html', context={'request': request, 'direction': DIRECTION, 'result': result})

@app.post('/')
def form_post(request: Request, zip: int = Form(...)):
    zip_instance = ZIP(zip)
    response = zip_instance.result()

    # if response['cod'] == '404':
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"zip {zip} : Does not exist"
    #     )

    forecast_instance = FORECAST(response['lat'], response['lon'])
    response = forecast_instance.result()
    parser_instance = PARSER(response)

    result = parser_instance.datalist()
    return templates.TemplateResponse('form.html', context={'request': request, 'direction': DIRECTION, 'result': result, 'zip': zip})

    
    
# f.close()