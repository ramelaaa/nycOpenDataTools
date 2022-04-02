#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata

pd.options.display.max_columns = None
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
client = Socrata("data.cityofnewyork.us", None)

whereClause = "charge_1_code_description='OPERATING EMISSION SOURCE WITH EXPIRED REGISTRATION'AND violation_location_borough='BRONX'"

# tickets = client.get("jz4z-kudi",where="(issuing_agency='SANITATION DEPT'OR issuing_agency='SANITATION OTHERS' OR issuing_agency='SANITATION RECYCLING')AND violation_location_borough='BRONX'",limit=100000)
tickets= client.get("jz4z-kudi",where=whereClause,limit=100000)
tickets_df = pd.DataFrame.from_records(tickets)

tickets_df["penalty_imposed"] = pd.to_numeric(tickets_df["penalty_imposed"])
tickets_df["paid_amount"] = pd.to_numeric(tickets_df["paid_amount"])

print("Penalty imposed $:",tickets_df["penalty_imposed"].sum())
print("Paid: $", tickets_df["paid_amount"].sum())
print(tickets_df["penalty_imposed"].describe())
print(tickets_df["hearing_status"].value_counts())






