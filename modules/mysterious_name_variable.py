"""
** __name__**
-when run, every python file has a __name__variable
-if the file is the main file being run, its variable is __main__

"""


def say_hi():
    print("Hi! My __name__ is [__name__}")


# when importing files with dunder variables. the imported value is the file name
# if its the main file, the dunder variable has the value of main


"""
ignoring code on import 

if ""__name__"" == " __main__":
    -this code will only run
    if the file is the main file! 
"""
