#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata

pd.options.display.max_columns = None
pd.set_option('display.max_colwidth', None)
client = Socrata("data.cityofnewyork.us", None)

dataset_id = "jz4z-kudi"

lastname    = "respondent_last_name='RAMNAUTH'"
surujnauth  = "respondent_first_name='SURUJNAUTH'"
toumwatee   = "respondent_first_name='TOUMWATEE'"
ramela      = "respondent_first_name='RAMELA'"
sANDt       = "respondent_first_name='SURUJNAUTHTOUMWAT'"

borough = "violation_location_borough='BRONX'"
block   = "violation_location_block_no='03997'"
lot     = "violation_location_lot_no='0068'"

responseLimit = 20

surujnauthQuery          = client.get(dataset_id,where=lastname + " AND " + surujnauth ,limit=responseLimit)
toumwateeQuery           = client.get(dataset_id,where=lastname + " AND " + toumwatee,limit=responseLimit)
ramelaQuery              = client.get(dataset_id,where=lastname + " AND " + ramela ,limit=responseLimit)
surujnauthtoumwatQuery   = client.get(dataset_id,where=sANDt,limit=responseLimit)
homeQuery                = client.get(dataset_id,where= borough + " AND " + block + " AND " + lot,limit = responseLimit)

# Create DataFrames for each data set
toumwatee_df            = pd.DataFrame.from_records(toumwateeQuery)
ramela_df               = pd.DataFrame.from_records(ramelaQuery)
surujnauth_df           = pd.DataFrame.from_records(surujnauthQuery)
surujnauthtoumwat_df    = pd.DataFrame.from_records(surujnauthtoumwatQuery)
home_df                 = pd.DataFrame.from_records(homeQuery)

# print rresuls 
print("- Surujnauth Ramnauth: ")
if surujnauth_df.empty:
    print ("No Tickets")
else:
    print("Ticket Number: " + surujnauth_df["ticket_number"] + "  Paid:$" + surujnauth_df["paid_amount"] + " " + surujnauth_df["issuing_agency"])

print("- Toumwatee Ramnauth: ")
if toumwatee_df.empty:
    print ("No Tickets")
else:
    print("Ticket Number: " + toumwatee_df["ticket_number"] + " Paid:$" + toumwatee_df["paid_amount"]+ " " + toumwatee_df["issuing_agency"])

print("- Surujnauth and Toumwatee Ramnauth: ")
if surujnauthtoumwat_df.empty:
    print ("No Tickets")
else:
    print("Ticket Number: " + surujnauthtoumwat_df["ticket_number"] + "  Paid:$" + surujnauthtoumwat_df["paid_amount"]+ " " + surujnauthtoumwat_df["issuing_agency"])

print("- Ramela Ramnauth: ")
if ramela_df.empty:
    print ("No Tickets")
else:
    print("Ticket Number: " + ramela_df["ticket_number"] + " Paid:$" + ramela_df["paid_amount"]+ " " + ramela_df["issuing_agency"])

print("- Home")
if home_df.empty:
    print ("No Tickets")
else:
    print("Ticket Number: " + home_df["ticket_number"] + " Paid:$" + home_df["paid_amount"] + " " + home_df["issuing_agency"] + " " + home_df["violation_date"] +" " +home_df["respondent_last_name"])
