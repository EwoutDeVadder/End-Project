import grabData
import calcData

class main():
    def __init__(self) -> None:
        self.data = grabData.websiteScriptManager()
        self.processData = calcData.dataProcessor()

x = main()

x.data.updateURL()
x.data.updatePriceList()
print(x.data.prices)
