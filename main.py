# All other 'libraries' are imported
# to this main file so it's easy to see
# where an error occurs.

import grabData

class processData():
    def __init__(self) -> None:
        self.data = grabData.websiteScriptManager()

process = processData()

process.data.changeURLLocation("BE")
process.data.updateURL()
process.data.updatePriceList()
print(process.data.prices)