# do multiple calculations with the aquired data.

# [COMPLETE] the average can be calculated for other calculations

# [COMPLETE] calculate the lowest of today

# [IN PROGRESS] calculate the highest price of today

# [IN PROGRESS] calculate the percentage between the average price and the lowest price and see
# how much power we chould charge for we need to calculate the second best option 
# if the user needs to charge their vehicle faster, like they set when the car
# should be fully charged, and then I calculate how the charge should go. 

#import math

class calculateData():
    def __init__(self) -> None:
        self.averagePrice = 0

    def calcAvrOfCurDay(self, priceList:list):
        result = 0.0
        for item in priceList:
            result += item
        self.averagePrice = result / len(priceList)
        return (self.averagePrice)
    
    def calcLowestOfCurDay(self, priceList:list):
        curLowestPrice = 9999
        for price in priceList:
            if price < curLowestPrice:
                curLowestPrice = price
        return curLowestPrice

    def calcHighestOfCurDay(self, priceList:list):
        pass
    
    def stateOfCharge(self):
        pass

