#Kolbeinn Ingólfsson
#Verkefni 4 - VEFII
#Controller

from MVC import app
from MVC import model
from flask import render_template, redirect, url_for, flash, request


laust = model.Laust(model.a1)

byggingar = model.byggingar


path = "main.tpl"

# selected_timi = laust.selected_time(10, 10, 2)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    file = "lausarstofur.tpl"
    current_timi = laust.current_time()
    return render_template(path, file=file, timi=current_timi, len=len(current_timi), byggingar=byggingar)


@app.route('/val', methods=['GET', 'POST'])
def val():
    file = "lausarstofur.tpl"
    timi = request.args.get("timi")
    if timi[0:2].isdigit() and timi[3:5].isdigit():
        print(timi)
        sel = list(map(int, timi.split(":")))
    else:
        return redirect(url_for("index"))
    selected_timi = laust.selected_time(sel[0], sel[1], 1)
    return render_template(path, file=file, timi=selected_timi, len=len(selected_timi), byggingar=byggingar)
