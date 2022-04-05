#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata
pd.set_option('display.max_columns', None) 
import os
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime

class oath:
    def __init__(self, *args):
        if(len(args) == 2):
            self.lastname = args[0]
            self.firstname = args[1]
            self.type = "name"
        elif(len(args) == 3):
            self.borough = args[0]
            self.block = args[1]
            self.lot = args[2]  
            self.type = "bbl" 
        else:
            "None" 
        self.client = Socrata("data.cityofnewyork.us", os.environ.get("TOKEN"))

    def getInfo(self):
        if(self.type == "name"):
            self.data = self.client.get("jz4z-kudi",where="respondent_last_name='" + self.lastname + "' AND respondent_first_name ='" + self.firstname + "'",limit=100000)

        if(self.type == "bbl"):
            self.data = self.client.get("jz4z-kudi",where="violation_location_borough='" + self.borough +"' AND violation_location_block_no='" +self.block + "' AND violation_location_lot_no = '" +self.lot +"'",limit=100000)

    def createDataFrame(self):
        self.violations_df = pd.DataFrame.from_records(self.data)

    def printUpdateTime(self):
        self.updatedTime = self.client.get_metadata("jz4z-kudi");
        self.time = datetime.fromtimestamp(self.updatedTime["viewLastModified"])
        print("Last updated on: ", self.time)

    def printData(self):
        if(len(self.violations_df)>0):
            if(self.type == "name"):
                print(len(self.violations_df), "ticket(s) found:", self.lastname, self.firstname)
            if(self.type == "bbl"):
                print(len(self.violations_df), "ticket(s) found:",self.borough, self.block, self.lot)
            print(self.violations_df[["ticket_number","issuing_agency","violation_date","penalty_imposed","paid_amount","respondent_last_name"]])
        else:
            if(self.type == "name"):
                print(self.lastname, self.firstname, ": No OATH violations found!")
            else:
                print(self.borough,self.block,self.lot ," : No OATH violations found!")