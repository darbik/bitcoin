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

def find_denominations(amount, availableBills):

    operation, amount = amount
    (fifties, twenties, tens, fives) = availableBills
    value = amount

    if operation == 'sell':

        remainder = amount
        nFifty = 0
        nTwenty = 0
        nTen = 0
        nFive = 0

        try:

            if remainder % 50 < 50 and fifties != 0:

                nFifty = amount / 50
                
                if nFifty > fifties:

                    while nFifty > fifties:

                        nFifty -= 1

                    remainder -= (nFifty * 50)
                    amount = remainder
                
                else:

                    remainder = remainder % 50
                    amount = remainder

        except:

            pass
        
        try:
            
            if remainder % 20 < 20 and twenties != 0:

                nTwenty = amount / 20
                
                if nTwenty > twenties:

                    while nTwenty > twenties:

                        nTwenty -= 1

                    remainder -= (nTwenty * 20)
                    amount = remainder
                
                else:

                    remainder = remainder % 20
                    amount = remainder

        except:

            pass

        try:

            if remainder % 10 < 10 and tens != 0:

                nTen = amount / 10
                
                if nTen > tens:

                    while nTen > tens:

                        nTen -= 1

                    remainder -= (nTen * 10)
                    amount = remainder
                
                else:

                    remainder = remainder % 10
                    amount = remainder

        except:

            pass

        try:

            if remainder % 5 < 5 and fives != 0:
                
                nFive = amount / 5
                
                if nFive > fives:

                    while nFive > fives:

                        nFive -= 1

                    remainder -= (nFive * 5)
                    amount = remainder

                else:

                    remainder = remainder % 5
                    amount = remainder

        except:

            pass
        
        if remainder != 0:

            option1 = value - remainder
            option2 = value + remainder

            answer = int(raw_input("Sorry we can't create a transaction for %i, but we can make a transaction for %i or %i, which do you want?" % (value, option1, option2)))

            if answer == option1:

                denominations = find_denominations(('sell', answer), availableBills)
            
            elif answer == option2:
                
                denominations = find_denominations(('sell', answer), availableBills)
            
        else:

            denominations = (nFifty, nTwenty, nTen, nFive)

        return denominations

