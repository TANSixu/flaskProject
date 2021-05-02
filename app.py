from flask import Flask
from flask import escape, url_for, render_template

app = Flask(__name__)


# @app.route('/home')
# def hello_world():
#     return '<h1>welcome to my watchlist!</h1>'

@app.route('/user/<name>')
def user_page(name):
    return 'user: %s'%escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('hello_world'))
    print(url_for('user_page', name='mars'))
    print(url_for('user_page', name='marstsx'))
    print(url_for('test_url_for'))
    return 'TEST page'

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/index')
def index():
    return render_template('index.html',name=name, movies=movies)

if __name__ == '__main__':
    app.run()
