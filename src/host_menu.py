import os
import pickle
from classes.user import Hosts, User

file_name = 'host_data'


#dump data in pickle file
# def dumper():

#load_data
# def load_guest():


def host_menu():
    #db = database
    # if not.is.file (pickle file) preceed normal
    if not os.path.isfile(file_name):
    #   else loadfile, then preceed
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

            host_dict.update({sign_mail:Guest(sign_name, sign_mail, sign_address)})
            
            #pickle gues_dict
            pickle.dump(host_dict,open(file_name,'wb'))
            # outfile.close()
    else: 
        # load_pickle_file
        host_data = pickle.load( open (file_name, 'rb'))   
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
            
            host_data.update({sign_mail:Hosts(sign_name, sign_mail, sign_address)})
            
            #pickle gues_dict
            pickle.dump(host_data,open(file_name,'wb'))
            # outfile.close()   
host_menu()

   

