from bs4 import BeautifulSoup
from selenium import webdriver

class BitcoinPrice:

    def fetchBTC(self, driver):

        driver.get("http://www.bfxdata.com/orderbooks/btcusd")

    def refreshBTC(self, driver):

        driver.refresh()
        html = driver.page_source
        soup = BeautifulSoup(html)
        btcString = soup.head.title.string
        btcPrice = ''

        for char in btcString:

            if char.isdigit:

                btcPrice += char

        print "Current Bitcoin price is : ", btcPrice

