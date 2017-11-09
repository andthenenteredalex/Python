""" Copyright Alex Clark September 2017
    
    This script takes input in Canadian dollars and outputs the USD amount. Functions perfectly on small amounts. Intended updates: take current exchange rate data and round all numbers perfectly.
    
    The first script I ever made all by myself, my idea, my trouble shooting, my creation. Not copied from a book.
    This came about while I was visiting Toronto and who, when they are learning to code and need a currency converter, doesn't write their own? =)
    
    Written in Python 3.5"""

def can_usd():
    can_amount = float(input("\nPlease enter the Canadian dollar amount I will be converting to USD: "))
    usd = (can_amount - (can_amount * 0.19)) # current exchange rate
    print(round(usd, 2)) 
    
can_usd()

