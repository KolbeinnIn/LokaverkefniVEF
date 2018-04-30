#Kolbeinn Ingólfsson
#Verkefni 4 - VEFII
#Controller

from MVC import app
from MVC import model
from flask import render_template, redirect, url_for, flash


laust = model.Laust(model.a1)

byggingar = model.byggingar
activate = model.activate


current_timi = laust.selected_time(10, 10, 2)
path = "main.tpl"

# current_timi = laust.current_time()
# selected_timi = laust.selected_time(10, 10, 2)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    file = "lausarstofur.tpl"
    return render_template(path, file=file) # , timi=current_timi)
