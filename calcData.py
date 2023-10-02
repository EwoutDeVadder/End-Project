import math

class dataProcessor():
    def __init__(self) -> None:
        pass

    def average(self, myList):
        result = 0.0
        for item in myList:
            result += item
        return (result / len(myList))
    
    def median(self, myList):
        result = 0.0
        self.sortList(myList)
        halfOfList = len(myList) / 2
        if halfOfList != round(halfOfList):
            halfOfList -= 0.5
            result = (myList[halfOfList] + myList[halfOfList+1]) / 2
        else:
            result = myList[halfOfList]     

        return result

    def sortList(self, myList):
        return myList.sort()