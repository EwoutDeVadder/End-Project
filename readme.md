## About the project ##
// Placeholder text //

## Changelog ##
# v0.6.1 #
* Continued on desktop.
* Added HACS -> Works
    - Configured HACS to work.
* Added OCPP -> Doesn't work because there's no chare point.
* Installation documentation on HACS says to use Linux 64 bit
  but 32 bit works aswell for me.
* To make it work I needed to add SSH as an integration.
    - Then open the SSH-terminal
    - Then run a command to install HACS
    - Add HACS as an integration
    - Configure HACS ( Requires a connection to github with a 6-figure key.)
    - Go to the new HACS tab to install OCPP
    - Configure OCPP
* 

# v0.6 #
* Tested with Virtual Machine, works on desktop,
  not at school on laptop. 
* Trying to add OCPP to project for Home Assistant.
  - I need HACS and Home Assistant on a VM.
  - VM working but Home Assistant is not.
  - Have not yet tried adding HACS due to HA not
    working.

# v0.5.2 #
* Added update function for easier readability
* BUGS:
    - [FIXED] Forgot to actually add the back to default values

# v0.5.1 #
* BUGS:
    - [FIXED] Delivery Date breaking when it's the first of any month
    - [ADDITION] Going too far back in time defaults time back to today.
        - Compares dates and sees if they match, if they don't, default to today's values.

# v0.5 #
* Date will automatically update again for QOL
* updatePriceList will now automatically make all values float-point values.
* added a main.py file to combine all 'libraries' and make a readable program. 
    - added class processData which automatically makes a variable data which is the
    websiteScriptManager.

* BUGS:
    - If delivery date is the first of any month trading date breaks.
    - If you go too far in time or back in time the website will default back to today.
    It should return an error when this happens.

# v0.4 #
* changeURLDate -> updateURLDate
    - Added offset so you can (optionally) add an offset to the date which is used.
* changeURLLocation now works and you can change the country to any valid country.
* Date wont automatically update after calling updateURL.

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

