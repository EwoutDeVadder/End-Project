# saving_data{
# 'date': datetime var
# 'todays_prices': []
# 'average_prices_today': 0
# }
import datetime
import json

class SaveData():
    def __init__(self, date: datetime, prices: list, averagePrices: float) -> None:
        self.saving_data = {
            'date': date,
            'todays_prices': prices,
            'average_prices_today': averagePrices
        }

    def localSave(self):
        pass

    def serverSave(self):
        pass


