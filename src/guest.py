from users import profile
from bookings import booking

class guest(profile):
    def bookings(self):
        self.bookings = []

    def add_booking(self):
        self.bookings.append(booking) 



#ryan.get_info()