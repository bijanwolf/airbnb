from host import hosts
from property import property


class property:
    def __init__(self, name, address, price):
        self.name = name
        self.address = address
        self.price  = price
        #booking