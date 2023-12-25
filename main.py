# All other 'libraries' are imported
# to this main file so it's easy to see
# where an error occurs.

import grabData
import calculateData
import datetime
import saveData

class processData():
    def __init__(self) -> None:
        self.data = grabData.websiteScriptManager()
        self.calc = calculateData.calculateData()

process = processData()

process.data.changeURLLocation("BE")
process.data.updateURL(1)
process.data.updatePriceList()
print(process.data.craftedUrl)
process.save = saveData.SaveData(process.data.date, process.data.prices)
process.save.tempLocalServerSave()