import pickle
from pick import pick

# def list_all_props():
host_data = pickle.load( open('host_data', 'rb')) 

title = 'Please choose a property'
# options = [i for i in host_data.values()]
options = ['1', '2', '3', '4']

option, index = pick(options, title, indicator='=>')

# list_all_props()