from flask import Flask,session,request,render_template,redirect,json
from conf import  *
from sqlalchemy import  *
import requests
import conf
from functions import  getAllBooks, get_user

app = Flask(__name__)
app.secret_key = 'No_secret_key'


@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/login/access',methods=['post','get'])
def loginAccess():

    username = request.form['username']
    password = request.form['password']

    getUser = get_user(username,password)

    if getUser == None:
        return render_template('login.html',error = 'Username or password are incorrect', errorCode=1)
    session['user_id'] = getUser['id']

    return  redirect('/index')

@app.route('/index', methods=['POST','GET'])
def index():
    if "user_id" not in session:
        return logout()
    result = getAllBooks(session['user_id'])
    return render_template('index.html', allBooks=result)


@app.route('/addBookIsbn',methods=['post','get'])
def addBookIsbn():
    isbn = request.form['isbn']

    result = getAllBooks(session['user_id'])

    if isbn =='':
        return render_template('index.html',allBooks=result, error="Please insert ISBN", errorCode=-1)

    link = 'https://www.googleapis.com/books/v1/volumes?q=isbn:'

    myRespons = requests.get(link+str(isbn))

    if myRespons.status_code != 200:
        return  render_template('index.html',allBooks=result,error="Google Api has some problem",errorCode=-1)
    myJson = json.loads(myRespons.content)
    if myJson['totalItems'] == 0:
        return render_template('index.html',allBooks=result, error="No book found", errorCode=-1)
    author = ''
    for item in myJson['items'][0]['volumeInfo']['authors']:
        author= author  + item + " "
    title = myJson['items'][0]['volumeInfo']['title']

    page_count = myJson['items'][0]['volumeInfo']['pageCount']
    if "averageRating" in myJson['items'][0]['volumeInfo'].keys():
        average_rating = myJson['items'][0]['volumeInfo']['averageRating']
    else:
        average_rating="This book doesn't have Average Rating"
    ins = insert(conf.BookCatalogue).values(
        title= title,
        author = author,
        page_count = page_count,
        average_rating = str(average_rating),
        user_id= session['user_id']
    )
    conf.connection.execute(ins)

    result = getAllBooks(session['user_id'])
    return render_template('index.html',allBooks=result, errorCode=1)

@app.route('/deleteBook/<int:id>')
def deleteBook(id):

    deleteSomeBook = delete(conf.BookCatalogue).where(conf.BookCatalogue.c.id == id)
    conf.connection.execute(deleteSomeBook)
    return redirect('index')


@app.route('/logout')
def logout():
    session.clear()

    return redirect("login")


app.run(host="0.0.0.0",debug=True)