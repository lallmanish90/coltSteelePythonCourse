"""
objectives 

- define what a module is 
-import code from built-in modules
-import code from other files
-import code from external modules using pip
-Describe the common module patterns
-Describe the request/response cycle in HTTP
-using the requests module to make requests to web apps 
"""
"""
why use modules ?

-helps keek python files small / dry
-can reuse code across multiple files by importing
-a module is just a Python file


"""
# **built in modules example**


import random as rand # this is how you can alias a module that is being imported
import random
print(random.choice(['apple', 'banana', 'cherry', 'orange']))

print(rand.choice(['apple', 'banana', 'cherry', 'orange']))

"""
** importing parts of a module**

- the FROM keyword lets you import part of a module 
-handy rule of thumb: only import what you need!
-if you still want to import everything , you can also use the 
from MODULE import *pattern
"""
"""
different ways to import 

- import random 
-import random as omg_so_random
-from random import *
-from random import choice, shuffle
-from random import choice as random_chooser
"""
"""
**creating custom modules**

-you can import from your own code too 
-the syntax is the same as before 
-import from the name of the python file

can import by using file name , does not require extension. Also needs to be in the same dir, 
else need to find the route for the file

import file

"""
# example


def fn():
    return "do some stuff"
