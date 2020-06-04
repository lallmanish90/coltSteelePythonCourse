"""
**kwargs
__ keyword Args 
- special operator we can pass to functions 
-gathers remaining keyword arguments as a dictionary 

- output will bring back 
"""



def fav_colors(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}'s favorite color is {value}")


fav_colors(colt="purple", ruby="red", ethel="teal")


def special_greeting(**kwargs):
    if "david" in kwargs and kwargs["david"] == "special":
        return "You get a special greeting David"
    elif "david" in kwargs:
        return f"{kwargs['david']} david!"
    return "not sure who this is ..."


# print(special_greeting(david="special"))
# print(special_greeting(saul="special"))
# print(special_greeting(david="hello"))
print(special_greeting(david="special", heather="hello"))
"""
this will allow you to go through key value pairs and loop through them without expicitly naming them in the 
parameter of the function. 
"""
