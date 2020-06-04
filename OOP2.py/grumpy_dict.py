class GrumpyDict(dict):
    def __repr__(self):
        print("none of your business")
        return super().__repr__()

    def __missing__(self, key):
        print(f"You want {key}? well it's not here")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY? ")
        print("OK FINE...")
        super().__setitem__(key, value)


data = GrumpyDict({'first': 'tom', 'animal': 'cat'})
print(data)
data["city"] = "tokyo"
print(data)
