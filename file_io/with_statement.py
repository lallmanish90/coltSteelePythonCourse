"""
with Blocks
* option 2


"""
#this will close the file
with open("file_io/short_story.txt") as file:
    data = file.read()
    print(data)
    print(file.read)
