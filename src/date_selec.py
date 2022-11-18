from datetime import date, datetime
from all_props import prop_selection

# function for choosing a date to see all available bookings


def data_selection():
    start = True
    while start == True:
        y, m, d = [int(x) for x in input('Type in the date of starting availability(yyyy/mm/dd):').split('/')]
        try:
            booking_start = date(y, m , d)
            start = False
        except:
            print('Date format was wrong, please type in the date again')
    end = True
    while end == True:
        y, m, d = [int(x) for x in input('Type in the date of ending availability(yyyy/mm/dd):').split('/')]
        try:
            booking_end = date(y, m , d)
            end = False
        except:
            print('Date format was wrong, please type in the date again') 
    res = prop_selection(booking_start, booking_end)
    
    # through the prop name finde the object of the class property in the host_data and add that object to booking in guest_data
    # then add a further logic loop to not only look if that property is available for the choosen booking date on the side of the host, but also if that property is not booked at that time
    # you get the property name the guest has decided to book 
    return res

# data_selection()