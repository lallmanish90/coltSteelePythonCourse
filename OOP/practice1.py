class Comment:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


svegs = Comment("svegs", "omg!", 4)
print(svegs.likes)
