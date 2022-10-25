import os
import pickle
from sign_in import sign_up
from classes.user import Guest, User


def guest_menu():
    file_name = 'guest_data'
    password = ""
    sign_name = ""
    sign_mail = ""
    sign_address = ""
    username = ""
    password1 = ""
    
    if not os.path.isfile(file_name):
        sign_up_res = sign_up(username, password, password1, sign_name, sign_mail, sign_address)
        sign_name = sign_up_res['sign_name']
        password =  sign_up_res['password']
        sign_mail = sign_up_res['sign_mail']
        sign_address = sign_up_res['sign_address']

        guest_dict = {}
        guest_dict.update({sign_mail:Guest(sign_name, password, sign_address)})
            
            #pickle gues_dict
        pickle.dump(guest_dict,open(file_name,'wb'))
            # outfile.close()
    else: 
        # load_pickle_file
        guest_data = pickle.load( open(file_name, 'rb'))   

        sign_up_res = sign_up(username, password, password1, sign_name, sign_mail, sign_address)
        # print(sign_up_res['sign_name'])
        sign_name = sign_up_res['sign_name']
        password =  sign_up_res['password']
        sign_mail = sign_up_res['sign_mail']
        sign_address = sign_up_res['sign_address']
            
        guest_data.update({sign_mail:Guest(sign_name, password, sign_address)})
            
            #pickle gues_dict
        pickle.dump(guest_data,open(file_name,'wb'))
            # outfile.close()   
guest_menu()


