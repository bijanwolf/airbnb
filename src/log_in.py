import pickle
import host_menu

def log_in():
    host_data = pickle.load( open(file_name, 'rb'))
    name = input("Enter your email:")
    pw = input("Enter your password:")

    try: 
        if host_data[name]:
            try:
                if pw == host_data[name]:
                    print("Login success")
                    # print("Hi %s"%host_data[username])
                else: 
                    print("Password or Email incorrect")
            except: 
                print("incorrect password or username")
        else: 
            print("Email does not exist")
    except:
        print("Login Error")


