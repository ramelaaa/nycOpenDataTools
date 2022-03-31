#!/usr/bin/env python

import pandas as pd
from sodapy import Socrata

pd.options.display.max_columns = None
pd.set_option('display.max_colwidth', None)
client = Socrata("data.cityofnewyork.us", None)

surujnauth = client.get("jz4z-kudi",where="respondent_last_name='RAMNAUTH' AND respondent_first_name='SURUJNAUTH' " ,limit=20)
toumwatee = client.get("jz4z-kudi",where="respondent_last_name='RAMNAUTH' AND respondent_first_name='TOUMWATEE' " ,limit=20)
ramela = client.get("jz4z-kudi",where="respondent_last_name='RAMNAUTH' AND respondent_first_name='RAMELA' " ,limit=20)
surujnauthtoumwat = client.get("jz4z-kudi",where="respondent_first_name='SURUJNAUTHTOUMWAT' " ,limit=20)
home = client.get("jz4z-kudi",where="violation_location_borough='BRONX' AND violation_location_block_no='03997' AND violation_location_lot_no='0068'",limit=20)

toumwatee_df = pd.DataFrame.from_records(toumwatee)
ramela_df = pd.DataFrame.from_records(ramela)
surujnauth_df = pd.DataFrame.from_records(surujnauth)
surujnauthtoumwat_df = pd.DataFrame.from_records(surujnauthtoumwat)
home_df = pd.DataFrame.from_records(home)
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
