list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(0, 3)}
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# # use the person variable in your answer
answer = {k: v for k, v in person}


answer = {vowel: 0 for vowel in "aeiou"}
answer = {a for a in chr(range(65, 90))}
answer = {chr(a) for a in range(65, 90)}

print(answer)
