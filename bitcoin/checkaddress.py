# To ensure the address is a valid bitcoin address

from bitcoin import is_address

def check_address(address):
    
    if is_address(address) is False: 

        while is_address(address) is False:

            address = raw_input("Invalid bitcoin address, please enter another address: ")
    
    if is_address(address):

        return address

