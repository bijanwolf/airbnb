import pickle
import host_menu

def log_in_host():
    host_data = pickle.load( open('host_data', 'rb'))
    mail = input("Enter your email:")
    pw = input("Enter your password:")

    try: 
        #if dic.has_key(key)
        if mail in host_data:
            try:
                if pw == host_data[mail][1]:
                    print("Login success")
                    print("Hi %s"%host_data[mail][0].name)
                else: 
                    print("Password or Email incorrect")
            except: 
                print("incorrect password or username")
        else: 
            print("Email does not exist")
    except:
        print("Login Error")


def log_in_guest():
    guest_data = pickle.load( open('guest_data', 'rb'))
    mail = input("Enter your email:")
    pw = input("Enter your password:")

    try: 
        if guest_data[mail]:
            try:
                if pw == guest_data[mail][1]:
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

log_in_host()