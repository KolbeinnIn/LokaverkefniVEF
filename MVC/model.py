# Kolbeinn Ingólfsson
# Verkefni 4 - VEFII
# Model
import sqlite3
import time

with sqlite3.connect("MVC/stofur.db") as db:
    cursor = db.cursor()


def get_time():
    now = time.localtime()
    return now


dagar = ["mánudagur",
         "þriðjudagur",
         "miðvikudagur",
         "fimmtudagur",
         "föstudagur",
         "laugardagur",
         "sunnudagur"]


a = cursor.execute("""SELECT stofur.nafn, stofur.ID, timar.timi_fra, timar.timi_til, timar.dagar_ID, stofur.bygging_ID
                        FROM stofur, timar
                        WHERE stofur.ID = timar.stofur_ID;""")
a1 = cursor.fetchall()


b = cursor.execute("""SELECT * FROM bygging;""")
byggingar = cursor.fetchall()


class Laust:
    def __init__(self, query):
        self.query = query
        self.nyr = []
    
    def selected_time(self, klst, minu, day, bygging):
        for x in self.query:
            flag = False
            fra, til = x[2].split(":"), x[3].split(":")
            timi = [x[0], x[1], [int(fra[0]), int(fra[1]), int(til[0]), int(til[1])], x[4], x[5]]
            if timi[2][2] >= klst >= timi[2][0] and timi[3] == day:
                if timi[2][0] == klst and timi[2][2] != klst:
                    if minu >= timi[2][1]:
                        flag = True
                elif timi[2][2] == klst and timi[2][0] != klst:
                    if minu <= timi[2][3]:
                        flag = True
                elif timi[2][2] == klst == timi[2][0]:
                    if timi[2][3] >= minu >= timi[2][1]:
                        flag = True
            if flag and bygging == 0:
                self.nyr.append(timi)
            elif flag and bygging != 0:
                if bygging == timi[-1]:
                    self.nyr.append(timi)
        return self.nyr
