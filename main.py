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

surujnauth = oath(lastname,firstName1)
surujnauth.getInfo()
surujnauth.createDataFrame()
surujnauth.printData()
print()

toumwatee = oath(lastname,firstName2)
toumwatee.getInfo()
toumwatee.createDataFrame()
toumwatee.printData()
print()

ramela = oath(lastname,firstName3)
ramela.getInfo()
ramela.createDataFrame()
ramela.printData()
print()

home = oath(borough,block,lot)
home.getInfo()
home.createDataFrame()
home.printData()
print()

hpdviolations = hpd(binNo)
hpdviolations.getInfo()
hpdviolations.createDataFrame()
hpdviolations.printData()
print()

dobviolations = dob(binNo)
dobviolations.getInfo()
dobviolations.createDataFrame()
dobviolations.printData()
print()

dobEcbviolations = dobEcb(binNo)
dobEcbviolations.getInfo()
dobEcbviolations.createDataFrame()
dobEcbviolations.printData()
print()

dobComplaints = dobComplaints(binNo)
dobComplaints.getInfo()
dobComplaints.createDataFrame()
dobComplaints.printData()
print()

threeOneOneBBL = threeOneOne(bbl)
threeOneOneBBL.getInfo()
threeOneOneBBL.createDataFrame()
threeOneOneBBL.printData()

print()
threeOneOneStreet = threeOneOne(street, borough)
threeOneOneStreet.getInfo()
threeOneOneStreet.createDataFrame()
threeOneOneStreet.printData()