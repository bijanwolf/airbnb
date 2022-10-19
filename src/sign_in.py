def sign_up():
        #db = database
        username = input("Create Username:")
        password = input("Create Password:")
        password1 = input("Confirm Password:")

        if password != password1:
            print("Password does not match! You need to restart.")
            sign_up()
        else: 
            print("""Account created successfully
finish sign in""")
            sign_name = input("Your first name:")
            sign_mail = input("Your e-mail address:")
            sign_address = input("Your streetname:")