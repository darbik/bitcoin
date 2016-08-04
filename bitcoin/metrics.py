from time import strftime

def get_volume(atmid, price, amount):
    
    volume = (atmid, price, amount)

    return volume

def get_time(atmid):

    time = (atmid, strftime("%Y-%m-%d %H:%M:%S"))       # time format is in UTC

    return time

def get_fees(atmid, price, amount):

    feesMade = (atmid, (amount / price) * 0.05)

    return feesMade

