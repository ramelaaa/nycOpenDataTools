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
surujnauth.print()
print()

toumwatee = oath(lastname,firstName2)
toumwatee.getInfo()
toumwatee.createDataFrame()
toumwatee.print()
print()

ramela = oath(lastname,firstName3)
ramela.getInfo()
ramela.createDataFrame()
ramela.print()
print()

home = oath(borough,block,lot)
home.getInfo()
home.createDataFrame()
home.print()
print()

hpdviolations = hpd(binNo)
hpdviolations.getInfo()
hpdviolations.createDataFrame()
hpdviolations.print()
print()

dobviolations = dob(binNo)
dobviolations.getInfo()
dobviolations.createDataFrame()
dobviolations.print()
print()

dobEcbviolations = dobEcb(binNo)
dobEcbviolations.getInfo()
dobEcbviolations.createDataFrame()
dobEcbviolations.print()
print()

dobComplaints = dobComplaints(binNo)
dobComplaints.getInfo()
dobComplaints.createDataFrame()
dobComplaints.print()
print()

threeOneOneBBL = threeOneOne(bbl)
threeOneOneBBL.getInfo()
threeOneOneBBL.createDataFrame()
threeOneOneBBL.print()

print()
threeOneOneStreet = threeOneOne(street, borough)
threeOneOneStreet.getInfo()
threeOneOneStreet.createDataFrame()
threeOneOneStreet.print()

