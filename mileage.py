print("how many kilometers did you run today")
kms = input("Add the distance you road your bike!")
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"your {kms}kms ride was {miles} miles!")
