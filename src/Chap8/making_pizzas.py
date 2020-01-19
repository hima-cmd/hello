'''
import pizzas
pizzas.make_pizza(16, 'pepperoni')
pizzas.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


from pizzas import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizzas import make_pizza as mp
mp(18, 'pepperoni')
mp(16, 'mushrooms', 'green peppers', 'extra cheese')

import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

'''
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
