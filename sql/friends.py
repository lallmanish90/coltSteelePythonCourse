import sqlite3

conn = sqlite3.connect("my_friends.db")
#create cursor object
c = conn.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends VALUES ('Merriewether','Lewis',7)'''

# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) values ('{form_first}')"
# BAD dont do it this way! ^^^^^^^^



# form_first = "Mary-Todd"
# query = f"INSERT INTO friends (first_name) values (?)"
# c.execute(query, (form_first,))
# # DO IT THIS WAY^^^^^^^^^^ this is a tuple



# data = ("Steve", "irwin", 9)
# query = "INSERT INTO friends VALUES (?,?,?)"
# c.execute(query, data)
# DO IT THIS WAY^^^^^^^^^^ this is a tuple

people = [
    ("Ronald", "amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)]

#c.executemany("INSERT INTO friends VALUES  (?,?,?)", people)
average = 0 
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    average += person[2]
print(average/len(people))

# c.execute(query,people)


#commit changes
conn.commit()
conn.close()
