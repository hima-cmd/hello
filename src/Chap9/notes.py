"""
In Python 2.7, inheritance is slightly different. 
The ElectricCar class would look like this:
   class Car(object):
        def __init__(self, make, model, year): 
        --snip--
   class ElectricCar(Car):
       def __init__(self, make, model, year):
           super(ElectricCar, self).__init__(make, model, year)
--snip--
"""
