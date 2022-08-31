import pickle
from classes.user import Guest, User

guest_dict = {}

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
        

        guest_dict.update({sign_mail:Guest(sign_name, sign_mail, sign_address)})
        # guest_dict[sign_mail] = Guest(sign_name, sign_mail, sign_address)
        # wird mein dict überschrieben, wegen der variable, oder wird es immer neu gestartet, wenn die funciton neu startet 
        # answer: die function setzt bei jedem neuen Start den dict wieder auf 0
        # der dict muss ausserhalb der function sein 
        
        # user1 = Guest(sign_name, sign_mail, sign_address)     
        # user1.get_info()  
guest_menu()
guest_menu()
guest_menu()

print("########################")
for key, value in guest_dict.items():
    print (key, value)
