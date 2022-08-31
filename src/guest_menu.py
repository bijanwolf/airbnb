import pickle
from classes.user import Guest, User

def guest_menu():
    #db = database
    username = input("Create Username:")
    password = input("Create Password:")
    password1 = input("Confirm Password:")

    if password != password1:
        print("Password does not match! You need to restart.")
        guest_menu()
    else: 
        print("""Account created successfully
finish sign in""")
        sign_name = input("Your first name:")
        sign_mail = input("Your e-mail address:")
        sign_address = input("Your streetname:")

        # guest_dict = {email: Guest(sign_name, sign_mail, sign_address)}
        guest_dict = {}

        guest_dict[sign_mail] = Guest(sign_name, sign_mail, sign_address), username, password1
        
        # for key, value in guest_dict.items():
        #     print (key, value.get_info())
        # user1 = Guest(sign_name, sign_mail, sign_address)     
        # user1.get_info()  
guest_menu()

