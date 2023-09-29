from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app= FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

@app.post("/")
def form_post(request: Request, zip: int = Form(...)):
    result = spell_number(zip)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})