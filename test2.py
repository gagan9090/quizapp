"""from test import *
sum(10,30)
mul(10,90)"""

# random module is imported

# importing random module
"""import random

random.seed(3)

# print a random number between 1 and 1000.
print(random.randint(1, 1000))

# if you want to get the same random number again then,
random.seed(3)
print(random.randint(1,1000))
"""
# If seed function is not used

from test import Find

a=Find()
a.find_area(90,90)


import random

#print(random.randint(1,20 , 90))
# remember this state
#state = random.getstate()

# print 10 random numbers
print(random.sample(range(20), k = 10))

# restore state
#random.setstate(state)

# print same first 5 random numbers
# as above
print(random.sample(range(20), k = 5))


list=[10,20,30,40,50,60]
print(random.choice(list))
#print(random.random.randrange(1,100))

# Gives totally unpredictable responses.
#print(random.randint(1, 1000))