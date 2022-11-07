import host_menu
import guest_menu
from log_in import *
from sign_in import *

# [x]sign_up as a guest, or host
# [x]log_in to an account 
# []see, or edit profile 
# []register properties as a guest 
# []host can seet availabilty of property
# []host can edit and see and manage his properties
# []guest can searh for available properties by filtering for location and date 
# []guests can book one property for a specific date 
# []guests can manage their bookings, view and cancel bookings

# if __name__ == "__main__":
#     main()

def main():
    opt = True
    while opt == True: 
        input_1 = input("Are you a host or a guest (h/g):")
        if input_1 == 'h':
            input_2 = input("Do you already have an account (y/n)")
            if input_2 == 'n':
                host_menu()
            elif input_2 == 'y':
                log_in_host()
        elif input_1 == 'g':
            input_3 = input("Do you already have an account")
            if input_3 == 'n':
                guest_menu()
            elif input_3 == 'y':
                log_in_guest()
        opt = False

# main()