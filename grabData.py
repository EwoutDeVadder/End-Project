from bs4 import BeautifulSoup
import requests 
import lxml
import datetime

class websiteScriptManager:
    def __init__(self) -> None:     
        # 3 PARAMETERS: AREA, TRADING DATE, DELIVERY DATE
        # + Rest of string 
        self.splitURL = [{
            'area_link': "https://www.epexspot.com/en/market-data?market_area=", 'area': "BE"},
            {'tradingdate_link' : "&trading_date=", 'tradingdate' : "2023-09-20"},
            {'deliverydate_link' : "&delivery_date=", 'deliverydate' : "2023-09-21"},
            "&underlying_year=&modality=Auction&sub_modality=DayAhead&technology=&product=60&data_mode=table&period=&production_period="]
        self.craftedUrl = ""
        self.requestValue = 0
        self.soup = BeautifulSoup()
        self.split = []
        self.prices = []

    def craftNewURL(self):
        self.craftedUrl = self.splitURL[0]['area_link'] + self.splitURL[0]['area']
        self.craftedUrl += self.splitURL[1]['tradingdate_link'] + self.splitURL[1]['tradingdate']
        self.craftedUrl += self.splitURL[2]['deliverydate_link'] + self.splitURL[2]['deliverydate']
        self.craftedUrl += self.splitURL[-1]
        #print(self.craftedUrl)

    def updateURL(self, offset = 0):
        self.updateURLDate(offset)

        self.craftNewURL()
        self.requestValue = requests.get(self.craftedUrl)
        self.soup = BeautifulSoup(self.requestValue.text, 'lxml')
    
    def updatePriceList(self):
        self.prices = self.soup.findAll('tr', class_="child")
        for index, unused in enumerate(self.prices):
            self.prices[index] = float(self.prices[index].text.split()[3])

    def updateURLDate(self, offsetInDays = 0):
        date = datetime.date.today()

        if offsetInDays != 0:
            date += datetime.timedelta(days=offsetInDays)

        self.splitURL[1]['tradingdate'] = str(date + datetime.timedelta(days= -1))
        self.splitURL[2]['deliverydate'] = str(date)

    def updateURLDate2(self, offsetInDays = 0):
        date = datetime.datetime.today()
        print(date.date)

    def changeURLLocation(self, location):
        self.splitURL[0]['area'] = location

# Testing
x = websiteScriptManager()
#x.updateURLDate2()
x.updateURL()
#x.makePriceList()
print(x.craftedUrl)

#x.craftNewURL()