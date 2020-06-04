"""
ask for age
18-21 wristband
21+ drink, normal entry
too young , sorry

"""

age = input("How old are you? ")
if age:
    age = int(age)

    if age >= 18 and age < 21:
        print("You can enter, but need a wristband")
    elif age >= 21:
        print(" you are good to enter and drink")
    else:
        print("you may not enter")
else:
    print("please enter an age")

    """
    in this lesson we learned about nesting and using truthy statements
    to get the desired output. This also had a catch in the form of 
    an else state ment that will return a message to the user if the 
    input was left empty.
    
    we also learned to change a string to an int so that it can be 
    compared and setting the variable int inside the conditinal.


    """
