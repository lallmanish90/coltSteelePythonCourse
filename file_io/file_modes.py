"""
**modes for opening files


-"r" , Read a file(no write) - this is the default
-"w" , this will write to the file, will overwrite the contents or create a new file
-"a" , this will append the contents to the end, cannot be moved with seek
-"r+", read and write to a file (writing based on a cursor) , by default will start at the begining
this mode will also only work if the file exists
"""
with open("file_io/short_story.txt", "r+") as file:
    file.seek(10)
    file.write(":) ")
    file.seek(20)
    file.write(":(")

def copy(file_name, new_file):
    with open(file_name) as file:
        text = file.read()

    with open(new_file, "w") as new_file:
        new_file.write(text)