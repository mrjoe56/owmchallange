# owmchallange
A challenge task working with owm APIs (api.openweathermap.org)

Please install/update all requirements before running the code. I am using "pip install -r requirements.txt"
Once completed, to run the webservice, I am using uvicorn like: "python3 -m uvicorn src.html:app --reload"

For more information about uvicorn capabilities (like binding to 0.0.0.0 etc.), please go to: https://www.uvicorn.org/settings/ 

In addition, please set an environment variable OWM_API_KEY='<you_own_api_key>'