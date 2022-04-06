#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata
pd.set_option('display.max_columns', None) 
import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class plates:
    """
    Constructor takes two parameters, a plate number and state abbreviation, both as strings
    In the Constructor,Socrata object is initiated to make api calls
    """
    def __init__(self, plateNumber, state):
        self.plateNumber = plateNumber
        self.state = state
        self.datasetID = "nc67-uf89"
        self.client = Socrata("data.cityofnewyork.us",  os.environ.get("TOKEN"))
        
    def getMetaData(self):
        self.meta = self.client.get_metadata(self.datasetID)

    """
    API call is made and stored in data
    """
    def getInfo(self):
        self.data = self.client.get(self.datasetID,where="plate='" + self.plateNumber + "'AND state ='" + self.state + "'",limit=100000)

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
            self.tickets_df.reset_index(inplace=True)
        else:
            print(self.plateNumber, ": No tickets found for:", self.plateNumber)
    
    def printMetadata(self):
        
        self.updatedTime = datetime.fromtimestamp(self.meta["rowsUpdatedAt"])
        print("Last updated on: ", self.updatedTime)

    """ 
        sum the amount of money owed
        print columns
    """
    def printData(self):
        if(len(self.tickets_df)>0):
            print(len(self.tickets_df), "tickets found",self.plateNumber, self.state)
            print("Amount Due: $",self.tickets_df["amount_due"].sum())
            print(self.tickets_df[["summons_number", "issue_date", "amount_due", "violation"]])