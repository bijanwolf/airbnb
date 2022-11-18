from datetime import date, datetime

class Property:
    def __init__(self, name, address, price, availability_start, availability_end):
        self.name = name
        self.address = address
        self.price  = price
        self.availability_start = availability_start
        self.availability_end = availability_end
        self.bookings = []

class Booking:
    def __init__(self, start_date, end_date, property, guest):
        self.start_date = start_date
        self.end_date = end_date
        self.property = property
        self.guest = guest

class User:
    def __init__(self, name, mail, address, password):
        self.name = name
        self.mail = mail
        self.address = address
        self.password = password

    def get_pers_info(self):
        print("Name:", self.name)
        print("Mail:", self.mail)
        print("Address:", self.address)
        print("Pasword:", self.password)
    
    def edit_info(self, new_name = None, new_mail = None, new_address = None):
        self.name = new_name if new_name is not None else self.name
        self.mail = new_mail if new_mail is not None else self.mail
        self.address = new_address if new_address is not None else self.address


class Guest(User):
    def __init__(self, name, mail, address, password):
        super().__init__(name, mail, address, password)
        self.bookings = []

    def add_booking(self):
        
        pass

    def get_booking_info(self): 
        pass
    
    def edit_booking(self):
        pass


class Hosts(User):
    def __init__(self, name, mail, address, password):
        super().__init__(name, mail, address, password)
        self.properties = []
    
    def get_prop_info(self):
        print()


    def edit_prop(self):
        pass




# Werner = Hosts('Werner', 'Wernermail', 'Werneradress', 'Wernerpw')
# print(Werner.name)
# Werner.get_info()
# Werner.add_properties()
# Werner.get_prop_info()
