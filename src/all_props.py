from classes.user import Hosts
from classes.user import Property
from classes.user import Booking
import pickle
from datetime import date, datetime
import sys

#selection menu, which lists all properties in a list, that are avaiable for booking, returns the prop names

def prop_selection( booking_start,  booking_end):
    # get the property out of the host_data
    host_data = pickle.load( open('host_data', 'rb')) 
    host_obj = [*host_data.values()]
    host_prop = [o.properties for o in host_obj]
    prop_obj = [item for sublist in host_prop for item in sublist]
    # only those properties, that are avaialbe for this date by the host
    prop_names = [o.name for o in prop_obj if o.availability_start <= booking_start and o.availability_end >= booking_end] 
    # filter the properties that are already booked during that time period
    book_names = [o.bookings for o in prop_obj]
    book_filter = [o.property for o in book_names if o.start_date < booking_start < o.end_date or o.start_date < booking_end < o.end_date]
    # cancel out the bookings in book_filter from prop_names
    filterd_prop = [o for o in prop_names if o not in book_filter]

    for i in filterd_prop: 
        print('{0}.{1}'.format(filterd_prop.index(i) +1, i))
    print('\n'*2)
    if len(filterd_prop) > 0:
        select = int(input('Choose the number of the Property you like:'))-1
    else: 
        print('There is no room available during that time')
    # gives you the name of the property you have selected    
    return(filterd_prop[select])
    

# date_0 = date(1996, 12, 1)
# date_1 = date(1997, 12, 1)
# prop_selection(date_0, date_1)