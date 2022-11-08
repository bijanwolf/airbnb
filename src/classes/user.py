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
        # start date
        start = True
        while start == True:
            y, m, d = [int(x) for x in input('Type in the date of starting availability(yyyy/mm/dd):').split('/')]
            try:
                prop_avai_start = date(y, m , d)
                start = False
            except:
                print('Date format was wrong, please type in the date again')
        # end date
        end = True
        while end == True:
            y, m, d = [int(x) for x in input('Type in the date of ending availability(yyyy/mm/dd):').split('/')]
            try:
                prop_avai_end = date(y, m , d)
                end = False
            except:
                print('Date format was wrong, please type in the date again')
        # list all available properties
        # add booking to booking in property and to booking of instance of guest
        pass
    
    def edit_booking(self):
        pass


class Hosts(User):
    def __init__(self, name, mail, address, password):
        super().__init__(name, mail, address, password)
        self.properties = []
    
    def get_prop_info(self):
        print(self.properties)

    def add_properties(self):
        prop_name = input('What is the name of the Property?:')
        prop_add = input('What is the address of your Property?:')
        prop_price = int(input('What is the price per night in €?:'))
        start = True
        while start == True:
            y, m, d = [int(x) for x in input('Type in the date of starting availability(yyyy/mm/dd):').split('/')]
            try:
                prop_avai_start = date(y, m , d)
                start = False
            except:
                print('Date format was wrong, please type in the date again')
        end = True
        while end == True:
            y, m, d = [int(x) for x in input('Type in the date of ending availability(yyyy/mm/dd):').split('/')]
            try:
                prop_avai_end = date(y, m , d)
                end = False
            except:
                print('Date format was wrong, please type in the date again')   
        self.properties.append(Property(prop_name, prop_add, prop_price, prop_avai_start, prop_avai_end))
    
    def edit_prop(self):
        pass




Werner = Hosts('Werner', 'Wernermail', 'Werneradress', 'Wernerpw')
# Werner.get_info()
Werner.add_properties()
Werner.get_prop_info()
