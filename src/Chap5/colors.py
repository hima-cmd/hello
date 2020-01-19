# if statements
# conditional tests
car = ['subaru','audi','bmw','ford']
for car in car:
    if car.lower() == 'subaru':
        print("If loop executed.")
        print("Is car == 'subaru'? I predict True.")
        print(car == 'subaru')
    elif car.lower() == 'audi':
        print("\n1st Else executed.")
        print("Is car == 'audi' ? I predict True.")
        print(car == 'audi')
    elif car.lower() == 'bmw':
        print("\n2nd Else executed.")
        print("Is car == 'bmw' ? I predict True.")
        print(car == 'bmw')
    else:
        print("\nLast else executed.")
        print("Is car == 'ford' ? I predict True.")
        print(car == 'ford')     
      