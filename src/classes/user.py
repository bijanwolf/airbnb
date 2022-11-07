class User:
    def __init__(self, name, mail, address, password):
        self.name = name
        self.mail = mail
        self.address = address
        self.password = password

    def get_info(self):
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


class Hosts(User):
    def __init__(self, name, mail, address, password):
        super().__init__(name, mail, address, password)
        self.properties = []

    def add_properties(self):
        pass

