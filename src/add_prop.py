import pickle
from datetime import date, datetime
from classes.user import Hosts
from classes.user import Property

def add_properties():

    host_data = pickle.load( open('host_data', 'rb')) 
    checker = True
    while checker == True:
        e_mail = input('Please sign state your sign-in mail:')
        if e_mail in host_data:
            checker = False
        else:
            print('Email typed in wrong')

    prop_name = input('What is the name of the Property?:')
    prop_add = input('What is the address of your Property?:')
    prop_price = int(input('What is the price per night in €?:'))
    start = True
    while start == True:
        y, m, d = [int(x) for x in input('Type in the date of starting availability(yyyy/mm/dd):').split('/')]
        try:
            prop_avai_start = date(y, m , d)
            start = False
        except:
            print('Date format was wrong, please type in the date again')
    end = True
    while end == True:
        y, m, d = [int(x) for x in input('Type in the date of ending availability(yyyy/mm/dd):').split('/')]
        try:
            prop_avai_end = date(y, m , d)
            end = False
        except:
            print('Date format was wrong, please type in the date again')  
            
    host_data[e_mail].properties.append(Property(prop_name, prop_add, prop_price, prop_avai_start, prop_avai_end))

    pickle.dump(host_data,open('host_data','wb'))
    #self.properties.append(Property(prop_name, prop_add, prop_price, prop_avai_start, prop_avai_end))

# add_properties()
# host_data = pickle.load( open('host_data', 'rb')) 
# host_data['ferdinandmail'].get_prop_info()