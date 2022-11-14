from classes.user import Hosts
from classes.user import Property
import pickle
from datetime import date, datetime
import sys


def prop_selection( booking_start,  booking_end):
    # start = datetime.time(0, 0, 0)
    # end = datetime.time(0, 0, 0)
    host_data = pickle.load( open('host_data', 'rb')) 
    host_obj = [*host_data.values()]
    host_prop = [o.properties for o in host_obj]
    prop_obj = [item for sublist in host_prop for item in sublist]
    prop_names = [o.name for o in prop_obj if o.availability_start <= booking_start and o.availability_end >= booking_end] 
    for i in prop_names: 
        print('{0}.{1}'.format(prop_names.index(i) +1, i))
    print('\n'*2)
    if 
    select = int(input('Choose the number of the Property you like:'))-1
    return(prop_names[select])
    

# date_0 = date(1996, 12, 1)
# date_1 = date(1997, 12, 1)
# prop_selection(date_0, date_1)