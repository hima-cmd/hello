# more nesting examples of dictionaries

cities ={
    'london':{
        'country':'uk',
        'approx_popul':'50m',
        'fact':'developed nation',
        },
    'new york':{
        'country':'usa',
        'approx_popul':'80k',
        'fact':'busiest place',
        },
    'new delhi':{
        'country':'india',
        'approx_popul':'10m',
        'fact':'capital',
        },
    }

# printing the info in cities dictionaries.

for city_names,city_info in cities.items():
    print('\nCity : '+city_names)
    print('Country : '+city_info['country'])
    print('Population : '+city_info['approx_popul'])
    print('Fact : '+city_info['fact'])
    
    