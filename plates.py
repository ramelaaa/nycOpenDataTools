#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata
pd.set_option('display.max_columns', None) 
import os
from os.path import join, dirname
from dotenv import load_dotenv

class plates:
    """
    Constructor takes two parameters, a plate number and state abbreviation, both as strings
    In the Constructor,Socrata object is initiated to make api calls
    """
    def __init__(self, plateNumber, state):
        self.plateNumber = plateNumber
        self.state = state
        self.client = Socrata("data.cityofnewyork.us",  os.environ.get("TOKEN"))

    """
    API call is made and stored in data
    """
    def getInfo(self):
        self.data = self.client.get("nc67-uf89",where="plate='" + self.plateNumber + "'AND state ='" + self.state + "'",limit=100000)

    """
    Data Frame is made from data
    """
    def createDataFrame(self):
        self.tickets_df = pd.DataFrame.from_records(self.data)

    """ 
        amount_due must be made to numeric to sum all the values
        issue date is converted to date to sort by it
        finally, sort by date
    """
    def cleanDataFrame(self):
        if(len(self.tickets_df)>0):
            self.tickets_df["amount_due"] = pd.to_numeric(self.tickets_df["amount_due"])
            self.tickets_df["issue_date"] = pd.to_datetime(self.tickets_df["issue_date"])
            self.tickets_df = self.tickets_df.sort_values(by="issue_date")
        else:
            print(self.plateNumber, ": No tickets found for:", self.plateNumber)

    """ 
        sum the amount of money owed
        print columns
    """
    def print(self):
        if(len(self.tickets_df)>0):
            print(len(self.tickets_df), "tickets found",self.plateNumber, self.state)
            print("Amount Due: $",self.tickets_df["amount_due"].sum())
            print(self.tickets_df[["summons_number", "issue_date", "amount_due", "violation"]])