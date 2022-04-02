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