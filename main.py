from plates import plates 
from oath import oath
from threeOneOne import threeOneOne
from hpd import hpd
from dob import dob
from dobEcb import dobEcb
from dobComplaints import dobComplaints

bin="2042259"
bbl="2039970068"
borough = "BRONX"
block = "03997"
lot = "0068"
street = "FULLER STREET"

print("OATH: SURUJNAUTH RAMNAUTH------------------------------")
surujnauth = oath("RAMNAUTH","SURUJNAUTH")
surujnauth.getInfo()
surujnauth.createDataFrame()
surujnauth.print()
print()
print("OATH: TOUMWATEE RAMNAUTH")
toumwatee = oath("RAMNAUTH","TOUMWATEE------------------------")
toumwatee.getInfo()
toumwatee.createDataFrame()
toumwatee.print()
print()
print("OATH: RAMELA RAMNAUTH----------------------------------")
ramela = oath("RAMNAUTH","RAMELA")
ramela.getInfo()
ramela.createDataFrame()
ramela.print()
print()
print("OATH: 2039970068----------------------------------------")
home = oath(borough,block,lot)
home.getInfo()
home.createDataFrame()
home.print()
print()
print("HPD Violations-----------------------------------------")
hpdviolations = hpd(bin)
hpdviolations.getInfo()
hpdviolations.createDataFrame()
hpdviolations.print()
print()
print("DOB Violations-----------------------------------------")
dobviolations = dob(bin)
dobviolations.getInfo()
dobviolations.createDataFrame()
dobviolations.print()
print()
print("DOB ECB violations-------------------------------------")
dobEcbviolations = dobEcb(bin)
dobEcbviolations.getInfo()
dobEcbviolations.createDataFrame()
dobEcbviolations.print()
print()
print("DOB Complaints----------------------------------------")
dobComplaints = dobComplaints(bin)
dobComplaints.getInfo()
dobComplaints.createDataFrame()
dobComplaints.print()
print()
print("311 Requests and Complaints---------------------------")
threeOneOneBBL = threeOneOne(bbl)
threeOneOneBBL.getInfo()
threeOneOneBBL.createDataFrame()
threeOneOneBBL.print()
print()
threeOneOneStreet = threeOneOne(street, borough)
threeOneOneStreet.getInfo()
threeOneOneStreet.createDataFrame()
threeOneOneStreet.print()

