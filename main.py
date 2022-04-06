from plates import plates 
from oath import oath
from threeOneOne import threeOneOne
from hpd import hpd
from dob import dob
from dobEcb import dobEcb
from dobComplaints import dobComplaints

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

binNo=os.environ.get("BIN")
bbl=os.environ.get("BBL")
borough = os.environ.get("BOROUGH")
block = os.environ.get("BLOCK")
lot = os.environ.get("LOT")
street = os.environ.get("STREET")
lastname = os.environ.get("LASTNAME")
firstName1 = os.environ.get("FN1")
firstName2 = os.environ.get("FN2")
firstName3 = os.environ.get("FN3")


x = plates("KDS3506","NY")
x.getInfo()
x.createDataFrame()
x.cleanDataFrame()
x.getMetaData()
x.printMetadata()
x.printData()
# print("OATH TICKETS AND HEARINGS ")
# surujnauth = oath(lastname,firstName1)
# surujnauth.printUpdateTime()
# surujnauth.getInfo()
# surujnauth.createDataFrame()
# surujnauth.printData()
# print()

# toumwatee = oath(lastname,firstName2)
# toumwatee.getInfo()
# toumwatee.createDataFrame()
# toumwatee.printData()
# print()

# ramela = oath(lastname,firstName3)
# ramela.getInfo()
# ramela.createDataFrame()
# ramela.printData()
# print()

# home = oath(borough,block,lot)
# home.printUpdateTime()
# home.getInfo()
# home.createDataFrame()
# home.printData()
# print("-----------------------------------------")


# print("HPD Violations")
# hpdviolations = hpd(binNo)
# hpdviolations.printUpdateTime()
# hpdviolations.getInfo()
# hpdviolations.createDataFrame()
# hpdviolations.printData()
# print("-----------------------------------------")

# print("DOB Violations")
# dobviolations = dob(binNo)
# dobviolations.printUpdateTime()
# dobviolations.getInfo()
# dobviolations.createDataFrame()
# dobviolations.printData()
# print("-----------------------------------------")

# print("DOB ECB Violations")
# dobEcbviolations = dobEcb(binNo)
# dobEcbviolations.printUpdateTime()
# dobEcbviolations.getInfo()
# dobEcbviolations.createDataFrame()
# dobEcbviolations.printData()
# print("-----------------------------------------")

# print("DOB Complaints")
# dobComplaints = dobComplaints(binNo)
# dobComplaints.printUpdateTime()
# dobComplaints.getInfo()
# dobComplaints.createDataFrame()
# dobComplaints.printData()
# print("-----------------------------------------")

# print("311 for 2423 Fuller Street")
# threeOneOneBBL = threeOneOne(bbl)
# threeOneOneBBL.printUpdateTime()
# threeOneOneBBL.getInfo()
# threeOneOneBBL.createDataFrame()
# threeOneOneBBL.printData()

# print()
# print("311 for FULLER STREET, BRONX")
# threeOneOneStreet = threeOneOne(street, borough)
# threeOneOneStreet.getInfo()
# threeOneOneStreet.createDataFrame()
# threeOneOneStreet.printData()