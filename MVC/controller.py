#Kolbeinn Ingólfsson
#Verkefni 4 - VEFII
#Controller

from MVC import app
from MVC import model
from flask import render_template, redirect, url_for, flash
from MVC.forms import LoginForm


leikarar = model.Leikari(model.dicta).listi()
path = "main.tpl"
uppl = ""
nafn = "Gestur"


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


@app.route('/leikarar', methods=['GET', 'POST'])
def templates():
    file = "leikarar.tpl"
    global nafn
    if nafn is not None:
        user = {'username': nafn}
    return render_template(path, file=file, leikarar=leikarar, uppl=uppl, user=user)


@app.route("/leikarar/<act>")
def ser_leikarar(act):
    file = "leikarar.tpl"
    global nafn
    if nafn is not None:
        user = {'username': nafn}
    if act[0] == "&":
        for x in leikarar.keys():
            if act[1:] == x:
                uppl = leikarar[act[1:]]
                uppl.append(act[1:])

    for key, value in leikarar.items():
        if act[1:] == key:
            return render_template(path, file=file, leikarar=leikarar, act=act, uppl=uppl, user=user)
    return redirect(url_for("templates"))




