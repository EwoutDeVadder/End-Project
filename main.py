import grabData

class processData():
    def __init__(self) -> None:
        self.data = grabData.websiteScriptManager()

x = processData()

x.data.changeURLLocation("DE-LU")
x.data.updateURL()
x.data.updatePriceList()
print(x.data.prices)
