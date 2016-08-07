# Test example of how the flow of the atm would work without a kivy frontend
# Has lots of print statements to help with testing and make things clearer while testing

from random import randint

btcPrice = 600.00
atmAmount = 7500.00
btcAmount = 8  # only need about 2/3 of atmamount in btc
buyFee = 1.05                         
sellFee = 1.05
go = 'y'                
feesMade = 0        # max $750 per transaction
volume = 0

while go == 'y':
    
    x = randint(5, 15)
    y = randint(5, 15)   # to simulate random price movements
    btcPrice += x
    btcPrice -= y

    if atmAmount > 7500:

        additionalBuyFee = (((atmAmount / 7500) - 1) * 0.35)
        additionalSellFee = (((atmAmount / 7500) - 1) * 0.35)
        buyBtcPrice = (buyFee + additionalBuyFee) * btcPrice
        sellBtcPrice = (sellFee + additionalSellFee) * btcPrice * 0.905 
    
    elif atmAmount < 7500:

        additionalBuyFee = (((atmAmount / 7500) - 1) * 0.35)
        additionalSellFee = (((atmAmount / 7500) - 1) * 0.35) 
        buyBtcPrice = (buyFee + additionalBuyFee) * btcPrice
        sellBtcPrice = (sellFee + additionalSellFee) * btcPrice * 0.905

    else:

        buyBtcPrice = buyFee * btcPrice    
        sellBtcPrice = sellFee * btcPrice * 0.905
   
    print "\nREAL BTC PRICE : ", btcPrice       # market price
    print "\nBuy BTC price : ", buyBtcPrice     # market price + fees
    print "Sell BTC price : ", sellBtcPrice 
    print "ATM amount : ", atmAmount        
    print "BTC amount : ", btcAmount
    print "Fees made in BTC : ", feesMade
    print "Volume in fiat : ", volume

    buyorsell = raw_input("\nBuy or sell?") 
    howmuch = int(raw_input("How much?"))

    if howmuch > 500 or howmuch <= 0:

        while True:

            print "Max $750, please try again."
            howmuch = int(raw_input("How much?"))

            if howmuch <= 500:

                break

    if buyorsell == 'buy':
         
        print "You just bought ", (howmuch / buyBtcPrice) * 0.95, " BTC"
        atmAmount += howmuch
        btcAmount -= (howmuch / buyBtcPrice) * 0.95
        feesMade += howmuch / buyBtcPrice * 0.05
        volume += howmuch

    if buyorsell == 'sell':

        print "You just sold", (howmuch / sellBtcPrice) * 0.95, " BTC"
        atmAmount -= howmuch
        btcAmount += (howmuch / sellBtcPrice) * 0.95 
        feesMade += howmuch / sellBtcPrice * 0.05 
        volume += howmuch
