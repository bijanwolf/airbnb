import os
import pickle
from classes.user import Hosts, User

file_name = 'host_data'

def sign_up(x,y,z, a, b, c):
        #db = database
        x = input("Create Username:")
        y = input("Create Password:")
        z = input("Confirm Password:")

        if y != z:
            print("Password does not match! You need to restart.")
            sign_up()
        else: 
            print("""Account created successfully
            finish sign in""")
            a = input("Your first name:")
            b = input("Your e-mail address:")
            c = input("Your streetname:")
            
            res_dict = {}
            res_dict.update({'sign_mail': b, 'sign_name': a, 'sign_address': c, 'password': x})
            print('############################################')
            print(res_dict)
            return res_dict


def host_menu():
    password = ""
    sign_name = ""
    sign_mail = ""
    sign_address = ""
    username = ""
    password1 = ""
    

    if not os.path.isfile(file_name):
    #   else loadfile, then preceed
        sign_up()

        host_dict = {}

        host_dict.update({sign_mail:Hosts(sign_name, password, sign_address)})
            
            #pickle gues_dict
        pickle.dump(host_dict,open(file_name,'wb'))
            # outfile.close()
    else: 
        # load_pickle_file
        host_data = pickle.load( open (file_name, 'rb'))   

        sign_up_res = sign_up(username, password, password1, sign_name, sign_mail, sign_address)
        
        print(sign_up_res['sign_name'])
        sign_name = sign_up_res['sign_name']
        password =  sign_up_res['password']
        sign_mail = sign_up_res['sign_mail']
        sign_address = sign_up_res['sign_address']

        host_data.update({sign_mail:Hosts(sign_name, password, sign_address)})
        print(host_data) 
            #pickle gues_dict
        pickle.dump(host_data,open(file_name,'wb'))
            # outfile.close()   
host_menu()

   

