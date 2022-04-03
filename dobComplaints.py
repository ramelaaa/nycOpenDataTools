#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata

class dobComplaints:
    """
    Constructor takes two parameters, a plate number and state abbreviation, both as strings
    In the Constructor,Socrata object is initiated to make api calls
    """
    def __init__(self, bin):
        self.bin = bin
        self.client = Socrata("data.cityofnewyork.us", None)

    """
    API call is made and stored in data
    """
    def getInfo(self):
        self.data = self.client.get("eabe-havv",where="bin='" + self.bin +"'",limit=100000)

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
            print(self.bin)
            print(self.data_df[["complaint_number","status"]])
        else:
            print("No DOB complaints")