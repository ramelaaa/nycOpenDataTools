mport pandas as pd
from sodapy import Socrata

pd.options.display.max_columns = None

client = Socrata("data.cityofnewyork.us", None)

hpd_results     = client.get("wvxf-dwi5",where="bin = '2042259' " ,limit=20)
dob_results     = client.get("3h2n-5cm9",where="bin = '2042259' ", limit=20)
dob_ecb_results = client.get("6bgk-3dad",where="bin = '2042259' ", limit=20)
dob_complaints  = client.get("eabe-havv",where="bin = '2042259' ", limit=20)

# Convert to pandas DataFrame
hpd_results_df     = pd.DataFrame.from_records(hpd_results)
dob_results_df     = pd.DataFrame.from_records(dob_results)
dob_ecb_results_df = pd.DataFrame.from_records(dob_ecb_results)
dob_complaints_df  = pd.DataFrame.from_records(dob_complaints)

if hpd_results_df.empty:
    display("NO HPD violations")
else:
    print("-----HPD-----")
    print(hpd_results_df)
    print("-----HPD-----")
    
if dob_results_df.empty:
    print("NO DOB violations")
else:
    print("-----DOB-----")
    print(dob_results_df)
    print("-----DOB-----") 
    
if dob_ecb_results_df.empty:
    print("NO DOB ECB violations")
else:
   print("-----DOB_ECB-----")
   print(dob_ecb_results_df)
   print("-----DOB_ECB-----")
    
if dob_complaints_df.empty:
    print("No DOB complaints")
else:
    print("-----DOB Complaints-----")
    print(dob_complaints_df)
    print("-----DOB Complaints-----")

