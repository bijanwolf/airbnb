def main():
    while True:
        choice = input(
            """
            Are you a Guest or a Host
            1. Host
            2. Guest
            """
        )

        if choice == "1":
            host_menu()
        elif choice == "2":
            guest_menu()
