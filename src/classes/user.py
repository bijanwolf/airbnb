class User:
    def __init__(self, name, mail, address):
        self.name = name
        self.mail = mail
        self.address = address

    def get_info(self):
        print("Name:", self.name)
        print("Mail:", self.mail)
        print("Address:", self.address)
    
    def edit_info(self, new_name = None, new_mail = None, new_address = None):
        self.name = new_name if new_name is not None else self.name
        self.mail = new_mail
        self.address = new_address


class Guest(User):
    def __init__(self, name, mail, address):
        super().__init__(name, mail, address)
        self.bookings = []

    def add_booking(self):
        pass


class Hosts(User):
    def __init__(self, name, mail, address):
        super().__init__(name, mail, address)
        self.properties = []

    def add_properties(self):
        pass
