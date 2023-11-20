# do multiple calculations with the aquired data.
# average, sort the list, and other usefull data which
# needs some complex or simple calculations.

#import math

class calculateData():
    def __init__(self) -> None:
        pass

    def calcAvrOfCurDay(self, myList):
        result = 0.0
        for item in myList:
            result += item
        return (result / len(myList))

    def sortList(self, myList):
        return myList.sort()