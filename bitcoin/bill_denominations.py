transaction = 320
remainder = transaction

while remainder != 0:
    
    nFifty = 0
    nfTwenty = 0
    nTen = 0
    nFive = 0

    try:

        if remainder % 50 < 50:

            nFifty = transaction / 50
            remainder = remainder % 50
            transaction = remainder

    except:

        pass
    
    try:

        if remainder % 20 < 20:

            nTwenty = transaction / 20
            remainder = remainder % 20
            transaction = remainder
   
    except:

        pass
    
    try:

        if remainder % 10 < 10:

            nTen = tranasaction / 10
            remainder = remainder % 10
            transaction = remainder
   
    except:

        pass

    try:

        if remainder % 5 < 5:

            nFive = transaction / 5
            remainder = remainder % 5
            transaction = remainder
  
    except:

        pass

print nFifty, nTwenty, nTen, nFive, transaction
