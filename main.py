from plates import plates 
from oath import oath
from threeOneOne import threeOneOne
from hpd import hpd
from dob import dob
from dobEcb import dobEcb
from dobComplaints import dobComplaints

binNo="2042259"
bbl="2039970068"
borough = "BRONX"
block = "03997"
lot = "0068"
street = "FULLER STREET"
lastname = "RAMNAUTH"
firstName1 = "SURUJNAUTH"
firstName2 = "TOUMWATEE"
firstName3 = "RAMELA"

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

