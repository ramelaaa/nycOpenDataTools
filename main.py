from plates import plates 
from oath import oath
from threeOneOne import threeOneOne
from hpd import hpd
from dob import dob
from dobEcb import dobEcb
from dobComplaints import dobComplaints

print("OATH: SURUJNAUTH RAMNAUTH------------------------------")
surujnauth = oath("RAMNAUTH","SURUJNAUTH")
surujnauth.getInfo()
surujnauth.createDataFrame()
surujnauth.print()

print("OATH: TOUMWATEE RAMNAUTH")
toumwatee = oath("RAMNAUTH","TOUMWATEE------------------------")
toumwatee.getInfo()
toumwatee.createDataFrame()
toumwatee.print()

print("OATH: RAMELA RAMNAUTH----------------------------------")
ramela = oath("RAMNAUTH","RAMELA")
ramela.getInfo()
ramela.createDataFrame()
ramela.print()

print("OATH: 2039970068----------------------------------------")
home = oath("BRONX","03997","0068")
home.getInfo()
home.createDataFrame()
home.print()

bin="2042259"

print("HPD Violations-----------------------------------------")
hpdviolations = hpd(bin)
hpdviolations.getInfo()
hpdviolations.createDataFrame()
hpdviolations.print()

print("DOB Violations-----------------------------------------")
dobviolations = dob(bin)
dobviolations.getInfo()
dobviolations.createDataFrame()
dobviolations.print()

print("DOB ECB violations-------------------------------------")
dobEcbviolations = dobEcb(bin)
dobEcbviolations.getInfo()
dobEcbviolations.createDataFrame()
dobEcbviolations.print()

print("DOB Complaints----------------------------------------")
dobComplaints = dobComplaints(bin)
dobComplaints.getInfo()
dobComplaints.createDataFrame()
dobComplaints.print()

print("311 Requests and Complaints---------------------------")
threeOneOneBBL = threeOneOne("2039970068")
threeOneOneBBL.getInfo()
threeOneOneBBL.createDataFrame()
threeOneOneBBL.print()

threeOneOneStreet = threeOneOne("FULLER STREET", "BRONX")
threeOneOneStreet.getInfo()
threeOneOneStreet.createDataFrame()
threeOneOneStreet.print()

