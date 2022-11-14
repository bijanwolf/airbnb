from datetime import date, datetime
from all_props import prop_selection

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
    print(res)

data_selection()