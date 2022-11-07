import pickle

def clear_pickle(file_name):
    data = pickle.load(open(file_name, 'rb')) 

    data.clear()

    pickle.dump(data,open(file_name,'wb'))

