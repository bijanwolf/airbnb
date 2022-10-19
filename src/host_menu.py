import os
import pickle
from classes.user import Hosts, User

file_name = 'host_data'

def sign_up():
        #db = database
        username = input("Create Username:")
        global password
        password = input("Create Password:")
        password1 = input("Confirm Password:")

        if password != password1:
            print("Password does not match! You need to restart.")
            sign_up()
        else: 
            print("""Account created successfully
finish sign in""")
            global sign_name
            sign_name = input("Your first name:")
            global sign_mail 
            sign_mail = input("Your e-mail address:")
            global sign_address 
            sign_address = input("Your streetname:")


def host_menu():
    #db = database
    # if not.is.file (pickle file) preceed normal
    if not os.path.isfile(file_name):
    #   else loadfile, then preceed
        sign_up()
    #     username = input("Create Username:")
    #     password = input("Create Password:")
    #     password1 = input("Confirm Password:")

    #     if password != password1:
    #         print("Password does not match! You need to restart.")
    #         host_menu()
    #     else: 
    #         print("""Account created successfully
    # finish sign in""")
    #         sign_name = input("Your first name:")
    #         sign_mail = input("Your e-mail address:")
    #         sign_address = input("Your streetname:")

    #         # guest_dict = {email: Guest(sign_name, sign_mail, sign_address)}
            
        host_dict = {}

        host_dict.update({sign_mail:Guest(sign_name, sign_mail, sign_address)})
            
            #pickle gues_dict
        pickle.dump(host_dict,open(file_name,'wb'))
            # outfile.close()
    else: 
        # load_pickle_file
        host_data = pickle.load( open (file_name, 'rb'))   
        sign_up()
    #     username = input("Create Username:")
    #     password = input("Create Password:")
    #     password1 = input("Confirm Password:")

    #     if password != password1:
    #         print("Password does not match! You need to restart.")
    #         host_menu()
    #     else: 
    #         print("""Account created successfully
    # finish sign in""")
    #         sign_name = input("Your first name:")
    #         sign_mail = input("Your e-mail address:")
    #         sign_address = input("Your streetname:")

    #         # guest_dict = {email: Guest(sign_name, sign_mail, sign_address)}
            
        host_data.update({sign_mail:Hosts(sign_name, sign_mail, sign_address)})
            
            #pickle gues_dict
        pickle.dump(host_data,open(file_name,'wb'))
            # outfile.close()   
host_menu()

   

