import host_menu
import guest_menu


# [x]sign_up as a guest, or host
# []log_in to an account and see, or edit profile 
# []register properties as a guest 
# []host can seet availabilty of property
# []host can edit and see and manage his properties
# []guest can searh for available properties by filtering for location and date 
# []guests can book one property for a specific date 
# []guests can manage their bookings, view and cancel bookings

def main():
    opt = True
    while opt == True: 
        input_1 = input("Do you already have an account (y/n)?")
        if input_1 == 'y':
            #login
            pass
        #sign_up
        elif input_1 == 'n':
            choice = input("1. is Host 2. is Guest choose 1/2 ?")
            if choice == '1':
                host_menu()
            elif choice == '2':
                guest_menu()


