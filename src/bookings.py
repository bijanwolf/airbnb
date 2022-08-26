from guest import guest
from property import property


class booking:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.property = property.name
        self.guest = guest.name
    
