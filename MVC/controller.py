#Kolbeinn Ingólfsson
#Verkefni 4 - VEFII
#Controller

from MVC import app
from MVC import model
from flask import render_template, redirect, url_for, flash
from MVC.forms import LoginForm


timar = model.timar

path = "main.tpl"


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def templates():
    file = "lausarstofur.tpl"
    return render_template(path, file=file, timar=timar)



"""
@app.route('/', methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    file = "login.tpl"
    form = LoginForm()
    global nafn
    nafn = form.username.data
    print(nafn)
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('templates'))

    return render_template(path, file=file, form=form)
"""