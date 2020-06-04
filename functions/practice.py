def multiple_letter_count(str):
    return {a: str.count(a) for a in str}


print(multiple_letter_count("helllooooooo"))
