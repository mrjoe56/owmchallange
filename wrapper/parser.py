# wrapper/parser.py

import json
import datetime as dt
from itertools import groupby
from .day import DAY 

class PARSER(object): # object's constructor get the json data
  def __init__(self, jsonresponse: json):
    self.jsonresponse = jsonresponse

  def print(self): # return the full object
    return self.jsonresponse

  def printkeys(self): # returns the keys
    return self.jsonresponse.keys() 

  def groupdays(self): # function to group the day's forecast in a dictionary
    sorteddictionary = dict()
    print("this is the json response", self.jsonresponse)
    contents = self.jsonresponse["list"] # get the content
    contents.sort(key=lambda content: dt.datetime.fromtimestamp(content['dt'])) # sort it based on epoch
    groups = groupby(contents, lambda content: dt.datetime.fromtimestamp(content['dt']).date()) # group it by date
    for date, group in groups: # itterate to create a list of forecasts
      innerlist = []
      for content in group:
        innerlist.append(content)
      day_instance = DAY(innerlist)
      sorteddictionary.update({date : day_instance}) # append to dictionary based on date
    return sorteddictionary # returns the sorted and group'd dictionary
  
  def datalist(self):
    days = self.groupdays()
    datalist = { 'Titles': ['Date' , 'Temperature', 'Precipitation'], 'Days': []}
    for key in days:
        datalist['Days'] += [days[key].sortedres()]
    return datalist