from bs4 import BeautifulSoup
import requests 
import lxml
import datetime

class websiteScriptManager:
    def __init__(self):     
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

    def craftNewURL(self):
        self.craftedUrl = self.splitURL[0]['area_link'] + self.splitURL[0]['area']
        self.craftedUrl += self.splitURL[1]['tradingdate_link'] + self.splitURL[1]['tradingdate']
        self.craftedUrl += self.splitURL[2]['deliverydate_link'] + self.splitURL[2]['deliverydate']
        self.craftedUrl += self.splitURL[-1]
        #print(self.craftedUrl)

    def updateURL(self):
        self.changeURLDate()
        self.craftNewURL()
        self.requestValue = requests.get(self.craftedUrl)
        self.soup = BeautifulSoup(self.requestValue.text, 'lxml')
    
    def makePriceList(self):
        self.prices = self.soup.findAll('tr', class_="child")
        for index, unused in enumerate(self.prices):
            self.prices[index] = self.prices[index].text.split()[3]
    def changeURLDate(self):
        today = datetime.date.today()
        self.splitURL[1]['tradingdate'] = str(today.year) + "-" + str(today.month) + "-" + str(today.day - 1)
        self.splitURL[2]['deliverydate'] = str(today)
    def changeURLLocation(self):
        return 0
        

# Testing
#x = websiteScriptManager()

#x.updateURL()
#x.makePriceList()
#print(x.prices)

#x.craftNewURL()