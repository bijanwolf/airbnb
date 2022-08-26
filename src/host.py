from users import profile
from property import property

class hosts(profile):
    pass
    def properties(self):
        self.properties = []

    def add_properties(self):
        self.properties.append(property) 

henry = hosts("tim", "tim@mail", "abcstreet")

henry.get_info()