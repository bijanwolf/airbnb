
from unicodedata import name


class profile:
    def __init__(self, name, mail, address):
        self.name = name
        self.mail = mail
        self.address = address

    def get_info(self):
        print("Name:", self.name)
        print("Mail:", self.mail)
        print("Address:", self.address)
        #return self.name, self.mail, self.address
    
    def edit_info(self, new_name, new_mail, new_address):
        self.name = new_name
        self.mail = new_mail
        self.address = new_address
        return self.name



