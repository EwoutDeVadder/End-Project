## About the project ##
// Placeholder text //

## Changelog ##

# v0.3 #
* changeURLtoToday -> changeURLDate
    - Works with today's date, library used: datetime
* When updating URL date is updated aswell and the updated URL is crafted also.

# v0.2 #
* Added seperated string link to easely modify date, country
* Added 2 functions to Class
    - changeURLtoToday
    - changeURLLocation

# v0.1 // Initial file transfer #
*  Added basic 'grabData.py' script
    - Grabs HTML from chosen website
    - Filters raw HTML to make a list of prices in EUR/MWh
* Added 'readme.md', 'info.md' to cleanly document changes.
* Started testing with Excell copy tables from website
    - Abandoned after libraries found for Python. (BeautifulSoup, requests, lxml)

## Sources ##
* Website Scraper:
    https://medium.com/analytics-vidhya/how-to-scrape-data-from-a-website-using-python-for-beginner-5c770a1fbe2d
*  Prices:
    https://www.epexspot.com/en/market-data?market_area=BE&trading_date=&delivery_date=2023-09-20&underlying_year=&modality=Continuous&sub_modality=&technology=&product=60&data_mode=table&period=&production_period=
* Pull prices in Excell: 
    https://www.youtube.com/watch?v=2yTAyVXzFGg&t=65s&ab_channel=Tutorialspoint

