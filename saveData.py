# saving_data{
# 'date': datetime var
# 'todays_prices': []
# 'average_prices_today': 0
# }
import datetime
import sqlite3

class SaveData():
    def __init__(self, date: datetime.date, prices: list) -> None:
        id = date.day + date.month * 100 + date.year * 10000
        print(id)
        self.saving_data = {
            'ID': id,
            'todays_prices': prices
        }

    def localSave(self):
        pass

    def serverSave(self):
        pass

    def tempLocalServerSave(self):
        con = sqlite3.connect('data.db')
        
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS tarieven (id INTEGER PRIMARY KEY, prices TEXT)''')

        values = (self.saving_data['ID'], ', '.join(str(price) for price in self.saving_data['todays_prices']))
        #print(values)
        cur.execute('''INSERT INTO tarieven (id, prices) VALUES (?, ?)''', values)
        con.commit()

        cur.close()
        con.close()