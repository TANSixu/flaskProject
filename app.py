from flask import Flask
from flask import escape, url_for

app = Flask(__name__)


@app.route('/home')
def hello_world():
    return '<h1>welcome to my watchlist!</h1>'

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

if __name__ == '__main__':
    app.run()
