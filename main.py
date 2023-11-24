# All other 'libraries' are imported
# to this main file so it's easy to see
# where an error occurs.

import grabData
import calculateData
import saveData

class processData():
    def __init__(self) -> None:
        self.data = grabData.websiteScriptManager()
        self.calc = calculateData.calculateData()

process = processData()

process.data.changeURLLocation("BE")
process.data.updateURL()
process.data.updatePriceList()
print(process.data.prices)
process.calc.calcAvrOfCurDay(process.data.prices)
print(process.calc.averagePrice)
print('-------------------------')
for price in process.data.prices:
    if price < process.calc.averagePrice:
        print(price)
    
print('-------------------------')
print(process.calc.calcLowestOfCurDay(process.data.prices))
