import os
import pickle
from classes.user import Guest, User

file_name = 'guest_data'


#dump data in pickle file
# def dumper():

#load_data
# def load_guest():


def guest_menu():
    #db = database
    # if not.is.file (pickle file) preceed normal
    if not os.path.isfile(file_name):
    #   else loadfile, then preceed
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

            guest_dict.update({sign_mail:Guest(sign_name, sign_mail, sign_address)})
            
            #pickle gues_dict
            pickle.dump(guest_dict,open(file_name,'wb'))
            # outfile.close()
    else: 
        # load_pickle_file
        guest_data = pickle.load( open (file_name, 'rb'))   
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
            
            guest_data.update({sign_mail:Guest(sign_name, sign_mail, sign_address)})
            
            #pickle gues_dict
            pickle.dump(guest_data,open(file_name,'wb'))
            # outfile.close()   
guest_menu()


