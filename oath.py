#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata

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
        self.client = Socrata("data.cityofnewyork.us", None)

    def getInfo(self):
        if(self.type == "name"):
            self.data = self.client.get("jz4z-kudi",where="respondent_last_name='" + self.lastname + "' AND respondent_first_name ='" + self.firstname + "'",limit=100000)

        if(self.type == "bbl"):
            self.data = self.client.get("jz4z-kudi",where="violation_location_borough='" + self.borough +"' AND violation_location_block_no='" +self.block + "' AND violation_location_lot_no = '" +self.lot +"'",limit=100000)

    def createDataFrame(self):
        self.violations_df = pd.DataFrame.from_records(self.data)

    def print(self):
        if(len(self.violations_df)>0):
            print(self.violations_df[["ticket_number","issuing_agency","violation_date","penalty_imposed","paid_amount","respondent_last_name"]])
        else:
            if(self.type == "name"):
                print(self.lastname, self.firstname, ": No OATH violations found!")
            else:
                print(self.borough,self.block,self.lot ," : No OATH violations found!")