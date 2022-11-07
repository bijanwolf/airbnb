class Property:
    def __init__(self, name, address, price, availability_start, availability_end ):
        self.name = name
        self.address = address
        self.price  = price
        self.availability_start = availability_start
        self.availability_end = availability_end
        self.bookings = []
