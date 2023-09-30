# wrapper/parser.py

import json
import datetime as dt
from itertools import groupby
from .day import Day 

class Parser(object): # object's constructor get the json data
  def __init__(self, json_res: json):
    self.json_res = json_res

  def print(self): # return the full object
    return self.json_res

  def printkeys(self): # returns the keys
    return self.json_res.keys() 

  def groupdays(self): # function to group the day's forecast in a dictionary
    sorted_dict = dict()
    contents = self.json_res["list"] # get the content
    contents.sort(key=lambda content: dt.datetime.fromtimestamp(content['dt'])) # sort it based on epoch
    groups = groupby(contents, lambda content: dt.datetime.fromtimestamp(content['dt']).date()) # group it by date
    for date, group in groups: # itterate to create a list of forecasts
      innerlist = []
      for content in group:
        innerlist.append(content)
      day_instance = Day(innerlist)
      sorted_dict.update({date : day_instance}) # append to dictionary based on date
    return sorted_dict # returns the sorted and group'd dictionary
  
  def datadict(self):
    days = self.groupdays()
    data_dict = { 'Titles': ['Date' , 'Temperature', 'Precipitation'], 'Days': []}
    for key in days:
        data_dict['Days'] += [days[key].sortedres()]
    return data_dict