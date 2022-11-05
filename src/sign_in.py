def sign_up(x,y,z, a, b, c):
        #db = database
        x = input("Create Username:")
        y = input("Create Password:")
        z = input("Confirm Password:")

        if y != z:
            print("Password does not match! You need to restart.")
            sign_up(x,y,z, a, b, c)
        else: 
            print("""Account created successfully
            finish sign in""")
            a = input("Your first name:")
            b = input("Your e-mail address:")
            c = input("Your streetname:")
            
            res_dict = {}
            res_dict.update({'sign_mail': b, 'sign_name': a, 'sign_address': c, 'password': y})
            return res_dict