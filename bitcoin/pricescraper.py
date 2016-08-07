from bs4 import BeautifulSoup
from selenium import webdriver

class BitcoinPrice:

    def fetchBTC(self, driver):

        driver.get("http://www.coindesk.com/price/")

    def refreshBTC(self, driver):

        driver.refresh()
        html = driver.page_source
        soup = BeautifulSoup(html)
        btcString = soup.head.title.string
        btcPrice = ''
        
        btcString = list(btcString.encode("utf-8"))

        for x in range(len(btcString)):
            
            if x is 10:     # only interested in the beginning of the string

                break

            if btcString[x].isdigit() or btcString[x] is '.':
                
                btcPrice += btcString[x] 
       
        btcPrice = float(btcPrice)
        
        return btcPrice

