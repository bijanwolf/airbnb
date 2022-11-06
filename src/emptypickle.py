import pickle

def clear_pickle(x):
    data = pickle.load(open(x, 'rb')) 

    data.clear()

    pickle.dump(data,open(x,'wb'))

clear_pickle('host_data')
