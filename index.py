from flask import Flask,render_template,request
import sqlite3

db = sqlite3.connect('StoryBoard.db')
cursor = db.cursor()
app = Flask(__name__)
#cursor.execute('CREATE TABLE stories(ID INTEGER PRIMARY KEY AUTOINCREMENT, Title varchar(16), Content nvarchar(255))')

@app.route('/',methods=['GET','POST'])
def index():
    row = cursor.execute('SELECT ID,Title FROM stories')
    return render_template('index.html', rows=row)

@app.route('/write', methods=['POST','GET'])
def add():
    if request.method == 'POST':   
        title = request.values.get('title')
        content = request.values.get('content')
        cursor.execute('INSERT INTO stories(Title, Content) VALUES(?,?)',(title,content))
        db.commit()
    return render_template('add.html')

@app.route('/<id>')
def post(id):
    details = cursor.execute('SELECT Title,Content FROM stories WHERE ID=?',(id,)).fetchall()
    return render_template('post.html',title=details[0][0],content=details[0][1])
app.run('0.0.0.0')
db.close()
