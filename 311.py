#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata
import sys
pd.set_option('display.max_rows', 200)
client  = Socrata("data.cityofnewyork.us", None)

dataset_id = "erm2-nwe9"
whereClause = "street_name = 'FULLER STREET'AND borough = 'BRONX'"
limit = 200000

_2423Fuller     = client.get(dataset_id,where= whereClause + " AND bbl = '2039970068'" ,limit=limit)
fuller_street   = client.get(dataset_id,where= whereClause + " AND status='Open'" ,limit=limit)

_2423Fuller_df   = pd.DataFrame.from_records(_2423Fuller)
fuller_street_df = pd.DataFrame.from_records(fuller_street)

_2423Fuller_df["created_date"] = pd.to_datetime(_2423Fuller_df["created_date"])
_2423Fuller_df = _2423Fuller_df.sort_values(by="created_date")

fuller_street_df["created_date"] = pd.to_datetime(fuller_street_df["created_date"])
fuller_street_df = fuller_street_df.sort_values(by="created_date")

print("- 2423 Fuller Street: 2039970068, all")
if(len(_2423Fuller_df)>0):
    print(_2423Fuller_df[["unique_key","descriptor","agency","status","created_date"]])
else:
    print(NONE)

print("- Fuller St, open cases only")
if(len(fuller_street_df)>0):
    print(fuller_street_df[["unique_key","descriptor","agency","bbl","created_date"]])
else:
    print(NONE)