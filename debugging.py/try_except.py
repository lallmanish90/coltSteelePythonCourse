try:
    foobar
except:
    print("PROBLEM")
print("after the try")


try:  # will try to run this first
    num = int(input("please enter a number: "))
except:  # will return error if not
    print("that is not a number")
else:  # will return this if error does not exist
    print("I'm in the else!")
finally:  # will always run at the end
    print("runs no matter what!")
