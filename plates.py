#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata

pd.options.display.max_columns = None
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
client = Socrata("data.cityofnewyork.us", None)

whereClause = "plate='KDS3506'"

# tickets = client.get("jz4z-kudi",where="(issuing_agency='SANITATION DEPT'OR issuing_agency='SANITATION OTHERS' OR issuing_agency='SANITATION RECYCLING')AND violation_location_borough='BRONX'",limit=100000)
tickets= client.get("nc67-uf89",where=whereClause,limit=100000)
tickets_df = pd.DataFrame.from_records(tickets)

tickets_df["amount_due"] = pd.to_numeric(tickets_df["amount_due"])
# tickets_df["payment_amount"] = pd.to_numeric(tickets_df["payment_amount"])

print(whereClause)
print("Amount Due $:",tickets_df["amount_due"].sum())
# print("Paid: $", tickets_df["payment_amount"].sum())

