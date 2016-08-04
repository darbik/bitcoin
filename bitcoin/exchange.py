def buy_bitcoin(price):

    amount = int(raw_input("How much do you want to buy?"))

    if amount > 750 or amount <= 5:

        while amount > 750 or amount <= 5:  # need to manage bill denominations in the safe

            amount = int(raw_input("Sorry please try another amount between $5 and $750."))
    
    amount = ('buy', amount)

    return amount

def sell_bitcoin(price):

    amount = int(raw_input("How much do you want to sell?"))

    if amount > 750 or amount <= 5:

        while amount > 750 or amount <= 5:

            amount = int(raw_input("Sorry please try another amount between $5 and $750."))
    
    amount = ('sell', amount)

    return amount

def calculate_fees(atmAmount):
    
    additionalFee = (((atmAmount / 7500) - 1) * 0.35)   

    return additionalFee


