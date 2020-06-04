"""
paremeter ordering 

order:
-parameters
-*args
-default parameters
-**kwargs
"""


def display_info(a, b, *args, instructor="colt", **kwargs):
    return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, last_name="steele", job="instructor"))


"""
a - 1 
b - 2 
args 3
instructor = "colt"        nothing was passed in , so default runs 

kwargs - {'last_name': steele", "job": "instructor"}
"""
