import sqlite3
#from flask import Flask

#app = Flask(__name__)

def connect_db():
    return sqlite3.connect('./mydatabase.db')

title = raw_input('title please')
text = raw_input('and the text')
db = connect_db()

db.execute('insert into entries (title, text) values (?, ?)',
                 [title,text])
db.commit()


cur = db.execute('select title, text from entries order by id desc')
entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]

print entries
