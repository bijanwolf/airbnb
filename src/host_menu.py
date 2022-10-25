import os
import pickle
from classes.user import Hosts, User
from sign_in import sign_up

def host_menu():
    file_name = 'host_data'
    password = ""
    sign_name = ""
    sign_mail = ""
    sign_address = ""
    username = ""
    password1 = ""
    

    if not os.path.isfile(file_name):
    #   else loadfile, then preceed
        sign_up_res = sign_up(username, password, password1, sign_name, sign_mail, sign_address)
        sign_name = sign_up_res['sign_name']
        password =  sign_up_res['password']
        sign_mail = sign_up_res['sign_mail']
        sign_address = sign_up_res['sign_address']

        host_dict = {}

        host_dict.update({sign_mail:Hosts(sign_name, password, sign_address)})
            
            #pickle gues_dict
        pickle.dump(host_dict,open(file_name,'wb'))
            # outfile.close()
    else: 
        # load_pickle_file
        host_data = pickle.load( open(file_name, 'rb'))   

        sign_up_res = sign_up(username, password, password1, sign_name, sign_mail, sign_address)
        print(host_data)
        # print(sign_up_res['sign_name'])
        sign_name = sign_up_res['sign_name']
        password =  sign_up_res['password']
        sign_mail = sign_up_res['sign_mail']
        sign_address = sign_up_res['sign_address']
        print('################')
        host_data.update({sign_mail:Hosts(sign_name, password, sign_address)})
        print(host_data) 
            #pickle gues_dict
        pickle.dump(host_data,open(file_name,'wb'))
            # outfile.close()   
        print(host_data)
host_menu()

   

