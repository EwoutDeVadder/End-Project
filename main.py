import grabData

class processData():
    def __init__(self) -> None:
        self.data = grabData.websiteScriptManager()

process = processData()

process.data.changeURLLocation("BE")
process.data.updateURL()
process.data.updatePriceList()
print(process.data.prices)