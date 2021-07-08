import sqlite3

db = sqlite3.connect('show.db')

show = db.execute("SELECT * FROM show")

db.commit()

db.close()

"50MIL"

likes = db.execute("SELECT likes FROM posts WHERE id = 'foo'")
likes = likes[0]
db.execute("UPDATE posts SET likes = ?", likes + 1)



print(f"My age is {age}")
print("My age is" + str(age))