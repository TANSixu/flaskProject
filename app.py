from flask import Flask
from flask import escape, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import click
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(20))

class Movie(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(60))
    year=db.Column(db.String(4))
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

@app.context_processor
def inject_user():
    user=User.query.first()
    return dict(user=user)

def forge():
    db.create_all()
    name = 'MarsTSX'
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

    user=User(name=name)
    db.session.add(user)
    for m in movies:
        movie=Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('Done.')
    
@app.errorhandler(404)
def page_not_found(e):
    # user=User.query.first()
    return render_template('404.html'),404


@app.route('/')
def index():
    # user=User.query.first()
    movies=Movie.query.all()
    return render_template('index.html',movies=movies)

if __name__ == '__main__':
    app.run()
