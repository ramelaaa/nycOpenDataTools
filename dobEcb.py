#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata
pd.set_option('display.max_columns', None) 
import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime

class dobEcb:
    """
    Constructor takes two parameters, a plate number and state abbreviation, both as strings
    In the Constructor,Socrata object is initiated to make api calls
    """
    def __init__(self, bin):
        self.bin = bin
        self.client = Socrata("data.cityofnewyork.us",  os.environ.get("TOKEN"))

    """
    API call is made and stored in data
    """
    def getInfo(self):
        self.data = self.client.get("6bgk-3dad",where="bin='" + self.bin +"'",limit=100000)

    """
    Data Frame is made from data
    """
    def createDataFrame(self):
        self.data_df = pd.DataFrame.from_records(self.data)


    def printUpdateTime(self):
        self.updatedTime = self.client.get_metadata("6bgk-3dad");
        self.time = datetime.fromtimestamp(self.updatedTime["rowsUpdatedAt"])
        print("Last updated on: ", self.time)

    """ 
        sum the amount of money owed
        print columns
    """
    def printData(self):
        if(len(self.data_df)>0):
            print(en(self.data_df),"ticket(s) found:", self.bin)
            print(self.data_df[["ecb_violation_number","ecb_violation_status","violation_type","issue_date","balance_due"]])
        else:
            print("No DOB ECB violations: ",self.bin)