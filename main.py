from plates import plates 
from oathClass import oath

oath1 = oath("RAMNAUTH", "SURUJNAUTH")
oath2 = oath("BRONX","03997","0068")



oath1.getInfo()
oath2.getInfo()

oath1.createDataFrame()
oath2.createDataFrame()

oath1.print()
oath2.print()


# plate = plates("HAC7330", "NY")
# plate.getInfo()
# plate.createDataFrame()
# plate.cleanDataFrame()
# plate.print()