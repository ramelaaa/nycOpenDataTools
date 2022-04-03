from plates import plates 
from oath import oath
from threeOneOne import threeOneOne
from hpd import hpd
from dob import dob
from dobEcb import dobEcb
from dobComplaints import dobComplaints

x = dobComplaints("1006562")
x.getInfo()
x.createDataFrame()
x.print()

# x = hpd("2042259")
# x.getInfo()
# x.createDataFrame()
# x.print()

# x = threeOneOne("2039970068")
# x.getInfo()
# x.createDataFrame()
# x.cleanDataFrame()
# x.print()

# y = threeOneOne("FULLER STREET","BRONX")
# y.getInfo()
# y.createDataFrame()
# y.cleanDataFrame()
# y.print()

# oath1 = oath("RAMNAUTH", "SURUJNAUTH")
# oath2 = oath("BRONX","03997","0068")

# oath1.getInfo()
# oath2.getInfo()

# oath1.createDataFrame()
# oath2.createDataFrame()

# oath1.print()
# oath2.print()


# plate = plates("HAC7330", "NY")
# plate.getInfo()
# plate.createDataFrame()
# plate.cleanDataFrame()
# plate.print()