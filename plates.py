#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata

class plates:
    def __init__(self, plateNumber, state):
        self.plateNumber = plateNumber
        self.state = state
        self.client = client = Socrata("data.cityofnewyork.us", None)

    def getInfo(self):
        self.data = self.client.get("nc67-uf89",where="plate='" + self.plateNumber + "'AND state ='" + self.state + "'",limit=100000)

    def createDataFrame(self):
        self.tickets_df = pd.DataFrame.from_records(self.data)
    
    def cleanDataFrame(self):
        self.tickets_df["amount_due"] = pd.to_numeric(self.tickets_df["amount_due"])
        self.tickets_df["issue_date"] = pd.to_datetime(self.tickets_df["issue_date"])
        self.tickets_df = self.tickets_df.sort_values(by="issue_date")

    def print(self):
        print(self.plateNumber, self.state)
        print("Amount Due: $",self.tickets_df["amount_due"].sum())
        print(self.tickets_df[["summons_number", "issue_date", "amount_due", "violation"]])