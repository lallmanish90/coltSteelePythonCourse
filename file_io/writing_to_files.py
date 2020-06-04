"""
writing files
-you can also use open to write to a file
-need to specify the "w" to the second argument
-write will OVERWRITE the current content with the "w" tag 
"""

# with open("file_io/short_story.txt", "w") as file:
#     file.write("writing file is great \n")
#     file.write("Here's another line of text \n")
#     file.write("Closing now , bye \n")
with open("file_io/lol.txt", "w") as file:
    file.write("haha \n" * 10000)