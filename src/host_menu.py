import pickle
from classes.user import Hosts, User

def host_menu():
    #db = database
    username = input("Create Username:")
    password = input("Create Password:")
    password1 = input("Confirm Password:")

    if password != password1:
        print("Password does not match! You need to restart.")
        host_menu()
    else: 
        print("""Account created successfully
finish sign in""")
        sign_name = input("Your first name:")
        sign_mail = input("Your e-mail address:")
        sign_address = input("Your streetname:")

        # guest_dict = {email: Guest(sign_name, sign_mail, sign_address)}
        host_dict = {}

        host_dict[sign_mail] = Hosts(sign_name, sign_mail, sign_address)
        
        for key, value in host_dict.items():
            print (key, value.get_info())
        # user1 = Guest(sign_name, sign_mail, sign_address)     
        # user1.get_info()  
host_menu()

