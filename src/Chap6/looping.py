#looping through dictionaries

rivers = {
    'egypt' : 'nile',
    'india': 'ganga',
    'china': 'yantze',
    }

for country, river in rivers.items():
    print("\nCountry :  "+country)
    print("River : " +river)
    print(" The "+
          river + " flows through "+
          country)
    
    
