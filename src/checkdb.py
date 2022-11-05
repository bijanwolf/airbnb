import pickle

def checkcdb():
    host_data = pickle.load( open('host_data', 'rb'))
    guest_data = pickle.load( open('guest_data', 'rb'))

    input1 = input('What do you want to see hostdb/guestdb:')

    if input1 == 'hostdb':
        print(host_data)
    elif input == 'guestdb':
        print(guest_data)

checkcdb()