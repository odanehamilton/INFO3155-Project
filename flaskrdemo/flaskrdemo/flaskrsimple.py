import sqlite3
from flask import Flask,g,render_template,flash,redirect,url_for

# sessions require secret keys
# just put it for now, we will 
# discuss later
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect('./mydatabase.db')

# db = connect_db()
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

# title = raw_input('title please')
# text = raw_input('and the text')
#db.execute('insert into entries (title, text) values (?, ?)',[title,text])
                 
#db.commit()
@app.route('/add', methods=['POST'])
def add_entry():
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))




# print entries
# cur = db.execute('select title, text from entries order by id desc')
# entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('entries.html', entries=entries)

if __name__ == '__main__':
    app.debug = True
    app.run()
