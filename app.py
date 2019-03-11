# -*- coding:utf-8-*-
from flask import url_for
from flask import Flask,render_template
import settings


app=Flask(__name__)
db =settings.db()
@app.route('/')
def index():
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
                {'title': 'WALL-E', 'year': '2008'},{'title': 'The Pork of Music', 'year': '2012'},
                ]   
    return render_template('index.html',name=name,movies=movies)

class User(db.Model):
    # 表名将会是 user(自动生成,小写处理)
    id = db.Column(db.Integer, primary_key=True)
    # 名字
    name = db.Column(db.String(20))
class Movie(db.Model):
    # 主键
    # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
    # 主键
    # 电影标题
    # 电影年份