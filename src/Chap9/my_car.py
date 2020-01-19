from car import Car 
from electric_car import ElectricCar

my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 22
my_new_car.read_odometer()
my_new_car.update_odometer(50)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013) 
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500) 
my_used_car.read_odometer()
my_used_car.increment_odometer(100) 
my_used_car.read_odometer()

'Creating instance of Child Class : Class ElectricCar' 
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_electric_car = ElectricCar('Jaguar' , 'model x' , 2019)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()
      
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())