#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata

class hpd:
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
        self.data = self.client.get("3h2n-5cm9",where="bin='" + self.bin +"'",limit=100000)

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
        print(self.bin)
        print(self.data_df[["violationid","class","inspectiondate","violationstatus"]])