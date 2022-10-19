def sign_up():
        #db = database
        username = input("Create Username:")
        global password
        password = input("Create Password:")
        password1 = input("Confirm Password:")

        if password != password1:
            print("Password does not match! You need to restart.")
            sign_up()
        else: 
            print("""Account created successfully
finish sign in""")
            global sign_name
            sign_name = input("Your first name:")
            global sign_mail 
            sign_mail = input("Your e-mail address:")
            global sign_address 
            sign_address = input("Your streetname:")
            