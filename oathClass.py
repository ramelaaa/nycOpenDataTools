#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata

class oath:
    def __init__(self, *args):
        if(len(args) == 2):
            self.lastname = args[0]
            self.firstname = args[1]
        elif(len(args) == 3):
            self.borough = args[0]
            self.block = args[1]
            self.lot = args[2]   
        else:
            "None" 