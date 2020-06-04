"""
**objectives
-read text files in python
-write text files in python
-use "with" blocks when reading/writing fields 
-describe the different ways to open a file
-read CSV files in python
-write CSV files in Python

**Reading Files
-you can read a file with the open function
-open returns a file object to you- returns more info besides what comes back from that file
-you can read a file object with the read method


example: 
file=open(story.txt)
file.read(story.txt)

**cursor movement 
-python reads files by using a cursor
-this is like the cursor you see when you're typeing
-after a file is read , the cursor goes to the end of the file 
-to move the cursor, use the seek method

file.seek(0) uses index to move the cursor in the file 

***if you only want one line of the doc at a time

file.readline()
- each time you run it , it will bring the following line
file.readlines() 
-will bring back all lines in a list in order of each line.


***closing files
 - with python you should close the files so that, the file will not take up resources
 -you can close a file with the close method
 -you can check if a file is closed with the closed attribute
 -always close files!

 



"""

file = open('file_io/short_story.txt')
# print(file.read())
file.seek(0)
print(file.readline())
print(file.readline())
print(file.closed)
file.close()
print(file.closed)
