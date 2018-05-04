#Kolbeinn Ingólfsson
#Verkefni 4 - VEFII
#Controller

from MVC import app
from MVC import model
from flask import render_template, redirect, url_for, request


byggingar = model.byggingar

path = "main.tpl"


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    laust = model.Laust(model.a1)
    file = "lausarstofur.tpl"
    ctimi = model.get_time()
    klst, minu, dagur = ctimi[3], ctimi[4], ctimi[6]
    current_timi = laust.selected_time(klst, minu, dagur, 0)
    return render_template(path, file=file, timi=current_timi, len=len(current_timi), byggingar=byggingar, flag=False, dagar=model.dagar)


@app.route('/val', methods=['GET', 'POST'])
def val():
    laust = model.Laust(model.a1)
    file = "lausarstofur.tpl"
    timi = request.args.get("timi")
    dagur = request.args.get("dagur")
    bygging = request.args.get("bygging")
    if timi[0:2].isdigit() and timi[3:5].isdigit():
        sel = list(map(int, timi.split(":")))
    elif timi == "":
        print("asd")
        sel = [model.get_time()[3], model.get_time()[4]]
    else:
        return redirect(url_for("index"))

    day = 0
    bygg = 0

    for x in dagur:
        if x.isdigit():
            if int(x) == 0:
                day = model.get_time()[6]+1
                print(day, "asd")
                break
            else:
                day = int(x)
                print(day, "asd2")
                break

    for x in bygging:
        if x.isdigit():
            bygg = int(x)
            break

    if day > 5:
        return redirect(url_for("index"))
    if bygg > 4:
        return redirect(url_for("index"))
    print(sel[0], sel[1])
    selected_timi = laust.selected_time(sel[0], sel[1], day, bygg)
    return render_template(path, file=file, timi=selected_timi, len=len(selected_timi), byggingar=byggingar, flag=True, dagar=model.dagar)
