#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata

class plates:
    def __init__(self, plateNumber, state):
        self.plateNumber = plateNumber
        self.state = state

    def printInfo(self):
        print(self.plateNumber)