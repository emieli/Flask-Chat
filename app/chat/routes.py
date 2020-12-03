from flask import render_template, session, request, copy_current_request_context, Blueprint, redirect, url_for
from wtforms import Form, StringField, validators, ValidationError

from .variables import users

chat = Blueprint('chat', __name__, template_folder = "templates", static_folder = "static")

def user_not_taken(form, field):
    if field.data in users:
        raise ValidationError('Username already in use, pick another')

@chat.route('/', methods = ["GET", "POST"])
def index():
    if not 'username' in session:
        return redirect(url_for('chat.login'))
    return render_template('index.html')

@chat.route('/login', methods = ["GET", "POST"])
def login():

    class LoginForm(Form):
        username = StringField('Username', [validators.Length(min=4, max=25), user_not_taken], render_kw={"placeholder": "Username"})

    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        session['username'] = request.form['username']
        return redirect(url_for('chat.index'))
        
    return render_template('login.html', form = form)
