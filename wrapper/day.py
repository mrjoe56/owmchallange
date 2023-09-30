# wrapper/day.py

import datetime as dt

class Day(object): # object's constructor get the list of forecasts of a day
  def __init__(self, forecastlist: list):
    self.forecastlist = forecastlist

  def printday(self): # return's the day's forcast list
    return self.forecastlist

  def daydate(self): # get's the date from the day object's first list item
    forecasts = self.forecastlist # get the list of forecasts for the day
    frmt_date = dt.datetime.utcfromtimestamp(forecasts[0]['dt']).strftime("%d/%m/%Y")
    return frmt_date

  def daymintemp(self): #get's the minimum temperature from the day's object (forcast list)
    forecasts = self.forecastlist # get the list of forecasts for the day
    forecast = min(forecasts, key=lambda ev: ev['main']['temp_min']) # find the minimum 
    return forecast['main']['temp_min']

  def daymaxtemp(self): # get's the maximum temperature from the day's object (forcast list)
    forecasts = self.forecastlist # get the list of forecasts for the day
    forecast = max(forecasts, key=lambda ev: ev['main']['temp_min']) # find the maximum
    return forecast['main']['temp_max']
  
  def daytotalprecipitation(self):
    forecast = 0 # default precipitation is always 0 (normal behaviour is that there is no rain)
    forecasts = self.forecastlist # get the list of forecasts for the day
    for item in forecasts: # itterate the items
      if 'rain' in item.keys(): # if you found the rain key in json response
        forecast += item['rain']['3h'] # add the amount for that specific day
    return forecast # return the amount of precipitation

  def sortedres(self): # this function is to sort the day responses as requested in the challange body
    tablelist = [
      self.daydate(), # the date
      str(round(self.daymaxtemp()))+"/"+str(round(self.daymintemp())), # the max/min temperature rounded like in the example
      round(self.daytotalprecipitation(),2) # the precipitation
    ]
    return tablelist