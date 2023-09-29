# tests/test.py

from wrapper.zip import ZIP
from wrapper.forecast import FORECAST
from wrapper.parser import PARSER
from wrapper.day import DAY

# zip_instance = ZIP(30318)
# response = zip_instance.result()
# print(response)

# forecast_instance = FORECAST(response['lat'], response['lon'])
# response = forecast_instance.result()
# print(response)

import json
f = open('test.json')
data = json.load(f)
parser_instance = PARSER(data)
days = parser_instance.groupdays()

# datalist = ['Date' , 'Temperature', 'Precipitation']
# for key in days:
#     datalist.append(days[key].sortedres())
#     # print(key, "->", days[key])
#     # print("date is: ", days[key].daydate())
#     # print("min temp is: ", days[key].daymintemp())
#     # print("max temp is: ", days[key].daymaxtemp())
#     # print("precipitation is: ", days[key].daytotalprecipitation())
# print(datalist)

print(parser_instance.datalist())


#print(data)
f.close()