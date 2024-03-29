import pandas as pd
from sodapy import Socrata
pd.set_option('display.max_columns', None) 


import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime

class threeOneOne:
    def __init__(self, *args):
        if(len(args) == 1):
            self.bbl = args[0]
            self.type = "bbl"
        elif(len(args) == 2):
            self.street = args[0]
            self.borough = args[1]
            self.type = "street"
        self.client = Socrata("data.cityofnewyork.us",  os.environ.get("TOKEN"))

    def getInfo(self):
        if(self.type == "bbl"):
            self.data = self.client.get("erm2-nwe9",where="bbl = '"+ self.bbl +"'" ,limit=2000)
        elif(self.type =="street"):
            self.data = self.client.get("erm2-nwe9",where="street_name = '" + self.street + "' AND borough = '"+ self.borough+ "' AND status='Open'" ,limit=2000)

    def createDataFrame(self):
        self.data_df = pd.DataFrame.from_records(self.data)

    def cleanDataFrame(self):
        if(len(self.data_df)>0): 
           self.data_df["created_date"] = pd.to_datetime(self.data_df["created_date"])
           self.data_df = self.data_df.sort_values(by="created_date")
        else:
            print("No 311 Service Requests or Complaints found.")

    def printUpdateTime(self):
        self.updatedTime = self.client.get_metadata("erm2-nwe9");
        self.time = datetime.fromtimestamp(self.updatedTime["rowsUpdatedAt"])
        print("Last updated on: ", self.time)


    def printData(self):
        if(len(self.data_df)>0):
            if(self.type == "bbl"):
                print(len(self.data_df), "item(s) found:", self.bbl)
                print(self.data_df[["unique_key","descriptor","agency","status","created_date"]])
            elif(self.type == "street"):
                print(len(self.data_df), "open item(s) found:", self.street, self.borough)
                print(self.data_df[["unique_key","descriptor","agency","bbl","created_date"]])
        else:
            print("no 311 complaints found")

       




