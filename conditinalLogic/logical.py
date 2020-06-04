age = 6
age > 2
age < 8
# you can set conditions by using AND and OR and NOT /
# does not have to be capitalized

# using AND
if age > 2 and age < 8:
    print("you pay child price")

# using OR
print("where do you live?")
city = input()


if city == "los angeles" or city == "san fran":
    print("you live in california")
else:
    print("you live somewhere else")


"""
overview is that there is two sides to the conditinals
If you want both sides to be a condition requirment use AND
if you only need one side to be true , use OR

"""
