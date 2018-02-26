# -*-coding:utf-8-*-
from flask import Flask,render_template,redirect,url_for
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
import sqlite3
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


app=Flask(__name__)
app.config['SECRET_KEY']='spider client'
bootstrap=Bootstrap(app)


class NameForm(Form):
    name=StringField('搜索内容：',validators=[Required()])
    submit=SubmitField('提交')

class post:
    def __init__(self,title,link):
        self.title=title
        self.link=link

@app.route('/',methods=['GET','POST'])
def index():
    form=NameForm()
    posts=[]
    if form.validate_on_submit():
        name=form.name.data
        conn=sqlite3.connect('spider/test.db')
        c=conn.cursor()
        cursor=c.execute("select title,link from posts;")
        for row in cursor:
            if re.search(name,row[0]):
                newpost=post(row[0],row[1])
                posts.append(newpost)
        c.close()
        conn.close()

    return render_template('base.html',form=form,posts=posts)

if __name__=='__main__':
    app.run(debug=True)









