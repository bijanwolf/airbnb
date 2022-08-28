def main():
    #while True:
        choice = input("""1. is Host
2. is Guest
choose 1/2 ?"""
                    )

        if choice == "1":
            host_menu()
        elif choice == "2":
            guest_menu()

main()