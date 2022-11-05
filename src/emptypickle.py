import pickle

def emptypickle():
    host_data = pickle.load( open('host_data', 'rb'))
    guest_data = pickle.load( open('guest_data', 'rb')) 

    host_data.clear()
    guest_data.clear()

    pickle.dump(host_data,open('host_data','wb'))
    pickle.dump(guest_data,open('guest_data','wb'))

emptypickle()