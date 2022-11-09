import pickle
from datetime import date, datetime
from classes.user import Guest
from classes.user import Booking

def add_booking():
    # start date
    host_data = pickle.load( open('host_data', 'rb')) 
    start = True
    while start == True:
        y, m, d = [int(x) for x in input('Type in the date of starting availability(yyyy/mm/dd):').split('/')]
        try:
            prop_avai_start = date(y, m , d)
            start = False
        except:
            print('Date format was wrong, please type in the date again')
    # end date
    end = True
    while end == True:
        y, m, d = [int(x) for x in input('Type in the date of ending availability(yyyy/mm/dd):').split('/')]
        try:
            prop_avai_end = date(y, m , d)
            end = False
        except:
            print('Date format was wrong, please type in the date again')
    # list all available properties
    
    # add booking to booking in property and to booking of instance of guest