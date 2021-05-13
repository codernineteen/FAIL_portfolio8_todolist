from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SECRET_KEY'] = 'asfkj&sj%kfh$23hf923@8fjs!'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DOWNLOAD_FOLDER'] = '/home/yc6936/mysite/files'
db = SQLAlchemy(app)


class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(64), nullable=False)


class AdditemForm(FlaskForm):
  description = StringField(
    "What are you going to do?",
    validators=[DataRequired()],
    render_kw={'style': 'width: 100ch'},
    )

db.create_all()

@app.route('/', methods=["GET","POST"])
def add_list():
  todo = Todo.query.all()
  form = AdditemForm()
  if request.method==['POST'] and form.validate_on_submit():
      new_item = Todo(text=request.form['description'])
      print(request.form['description'])
      db.session.add(new_item)
      db.session.commit()
      return redirect(url_for('add_list'))

  return render_template('index.html', form=form, todo=todo)