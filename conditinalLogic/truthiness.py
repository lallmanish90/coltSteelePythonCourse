animal = input(" what is your favorite animal?")

if animal:  # a non-empty string is truthy, while an empty string is falsey
    print(animal + ' is my favorite too!')
else:
    print("You didnt say anthing!")

"""
We can call values that will resolve to True as "truthy" , or
values that will resolve to False as "falsy".
Besides False conditional checks , other things that are naturally 
falsy include: empty objects, empty stings, None, and Zero.
"""
