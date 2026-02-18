Dollars = 100 # if money = 100 then buy 67 bitcoin
Dollars_Max = 999999 # stonks

def update_dollars():
    global Dollars
    if Dollars > Dollars_Max:
        Dollars = Dollars_Max

def add_dollars(amount):
    global Dollars
    Dollars += amount
    if Dollars > Dollars_Max:
        Dollars = Dollars_Max

def subtract_dollars(amount):
    global Dollars
    if amount <= Dollars:
        Dollars -= amount
        return True
    return False


