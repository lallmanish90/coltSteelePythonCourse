import sqlite3

conn = sqlite3.connect("my_friends.db")
# create Cursor Object 
c = conn.cursor()

c.execute("Select * from friends WHERE closeness > 5 ORDER BY closeness")
# for result in c:
#     print(result)
#fetches one result as a list 
# print(c.fetchone())
#feteches all results 
print(c.fetchall())
#commit changes
conn.commit()
conn.close()