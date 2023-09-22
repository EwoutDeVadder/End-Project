from bs4 import BeautifulSoup
import requests 
import lxml

class websiteScriptManager:
    def __init__(self):
        self.url = ""
        self.requestValue = 0
        self.soup = BeautifulSoup()
        self.split = []

    def changeURL(self, url):
        self.url = url
        self.requestValue = requests.get(self.url)
        self.soup = BeautifulSoup(self.requestValue.text, 'lxml')
    
    def makePriceList(self):
        self.prices = self.soup.findAll('tr', class_="child")
        for index, unused in enumerate(self.prices):
            self.prices[index] = self.prices[index].text.split()[3]


# Testing
x = websiteScriptManager()
x.changeURL("https://www.epexspot.com/en/market-data?market_area=BE&trading_date=2023-09-21&delivery_date=2023-09-22&underlying_year=&modality=Auction&sub_modality=DayAhead&technology=&product=60&data_mode=table&period=&production_period=")
x.makePriceList()
print(x.prices)