from bs4 import BeautifulSoup # pip install beautifulsoup4
import requests # pip install requests
import lxml # pip install lxml
import datetime # pip install datetime

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
        self.soup = BeautifulSoup()
        self.split = []
        self.prices = []
        self.today = datetime.datetime.today()

    def update(self, offsetInDays): # put offset to 1 to check if tomorrow is available, if not, it grabs today's prices.
        self.updateURL(offsetInDays)
        if self.compareDates() == False:
            ValueError("OFFSET DATE ERROR: we will default back to today's prices.")
            self.updateURL(0) 

        self.updatePriceList()

    def craftNewURL(self):
        self.craftedUrl = self.splitURL[0]['area_link'] + self.splitURL[0]['area']
        self.craftedUrl += self.splitURL[1]['tradingdate_link'] + self.splitURL[1]['tradingdate']
        self.craftedUrl += self.splitURL[2]['deliverydate_link'] + self.splitURL[2]['deliverydate']
        self.craftedUrl += self.splitURL[-1]

    def updateURL(self, offsetInDays = 0):
        self.updateURLDate(offsetInDays)

        self.craftNewURL()
        requestValue = requests.get(self.craftedUrl)
        self.soup = BeautifulSoup(requestValue.text, 'lxml')
    
    def updateURLDate(self, offsetInDays = 0):
        self.date = datetime.date(self.today.year, self.today.month, self.today.day)

        if offsetInDays != 0:
            self.date += datetime.timedelta(days=offsetInDays)

        self.splitURL[1]['tradingdate'] = str(self.date + datetime.timedelta(days= -1))
        self.splitURL[2]['deliverydate'] = str(self.date)

    def updatePriceList(self):
        self.prices = self.soup.findAll('tr', class_="child")
        for index, unused in enumerate(self.prices):
            self.prices[index] = float(self.prices[index].text.split()[3])
        
    def changeURLLocation(self, location):
        self.splitURL[0]['area'] = location

    def compareDates(self):
        siteDateSoup = self.soup.find(class_="last-update")
        siteDateSoup = siteDateSoup.text.split()[2:5]
        for index, months in enumerate(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]):
            if siteDateSoup[1] == months:
                siteDateSoup[1] = index + 1
        siteDate = datetime.date(int(siteDateSoup[2]),int(siteDateSoup[1]),int(siteDateSoup[0]))
        siteDate += datetime.timedelta(days=1)
        if self.date == siteDate:
            return True
        return False
