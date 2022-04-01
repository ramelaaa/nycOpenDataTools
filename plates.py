#!/usr/bin/env python
import pandas as pd
from sodapy import Socrata
import sys

client = Socrata("data.cityofnewyork.us", None)
if(len(sys.argv) != 3):
    print("Expected three arguments")
    print("python3 plates.py [plate] [state]")
    exit()

whereClause = "plate='" + sys.argv[1] + "' AND state = '" + sys.argv[2] + "'"
tickets= client.get("nc67-uf89",where=whereClause,limit=100000)
tickets_df = pd.DataFrame.from_records(tickets)
ticket = "amount_due"
tickets_df[ticket] = pd.to_numeric(tickets_df[ticket])
tickets_df["issue_date"] = pd.to_datetime(tickets_df["issue_date"])
print("Plate: ",sys.argv[1])
print("Amount Due: $",tickets_df[ticket].sum())
tickets_df = tickets_df.sort_values(by="issue_date")
print(tickets_df[["summons_number", "issue_date", ticket, "violation"]])