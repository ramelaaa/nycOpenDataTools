#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata

import os
from os.path import join, dirname
from dotenv import load_dotenv

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


    """ 
        sum the amount of money owed
        print columns
    """
    def print(self):
        if(len(self.data_df)>0):
            print(en(self.data_df),"ticket(s) found:", self.bin)
            print(self.data_df[["ecb_violation_number","ecb_violation_status","violation_type","issue_date","balance_due"]])
        else:
            print("No DOB ECB violations: ",self.bin)