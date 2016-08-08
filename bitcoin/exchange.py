def buy_bitcoin(price):

    amount = int(raw_input("How much do you want to buy?"))

    if amount > 500 or amount < 5:

        while amount > 500 or amount < 5: 

            amount = int(raw_input("Sorry please try another amount between $5 and $500."))
    
    amount = ('buy', amount)

    return amount

def sell_bitcoin(price):

    amount = int(raw_input("How much do you want to sell?"))

    if amount > 500 or amount < 5:

        while amount > 500 or amount < 5:

            amount = int(raw_input("Sorry please try another amount between $5 and $500."))
    
    amount = ('sell', amount)

    return amount

def calculate_fees(atmAmount):
    
    additionalFee = (((atmAmount / 7500) - 1) * 0.35)   

    return additionalFee

def display_transaction(amount, price):

    operation, amount = amount
    
    if operation == 'buy':

        print "You are buying %.8f bitcoin." % (amount / price * 0.95) 

    elif operation == 'sell':

        print "You are selling %.8f bitcoin." % (amount / price * 0.95)
    
    print "Your transaction costs %.8f bitcoin in fees." % (amount / price * 0.05)

def find_denominations(amount):

    operation, amount = amount
    
    if operation == 'sell':

        remainder = amount
        nFifty = 0
        nTwenty = 0
        nTen = 0
        nFive = 0

        try:

            if remainder % 50 < 50:

                nFifty = amount / 50
                remainder = remainder % 50
                amount = remainder

        except:

            pass
        
        try:
            
            if remainder % 20 < 20:

                nTwenty = amount / 20
                remainder = remainder % 20
                amount = remainder

        except:

            pass

        try:

            if remainder % 10 < 10:

                nTen = amount / 10
                remainder = remainder % 10
                amount = remainder

        except:

            pass

        try:

            if remainder % 5 < 5:

                nFive = amount / 5
                remainder = remainder % 5
                amount = remainder

        except:

            pass

        denominations = (nFifty, nTwenty, nTen, nFive)

        return denominations

