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
        self.pasa = [
            ["Pása", 1, [9, 10, 9, 15], 7, 0],
            ["Pása", 1, [10, 15, 10, 35], 7, 0],
            ["Pása", 1, [11, 35, 11, 40], 7, 0],
            ["Pása", 1, [12, 40, 13, 10], 7, 0],
            ["Pása", 1, [14, 10, 14, 15], 7, 0],
            ["Pása", 1, [15, 15, 15, 30], 7, 0],
            ["Pása", 1, [16, 30, 16, 35], 7, 0],
            ["Pása", 1, [17, 35, 17, 40], 7, 0]
        ]

    def selected_time(self, klst, minu, day, bygging):
        if ((klst == 18 and minu > 40) or (klst > 19)) or \
                ((klst < 8 and minu < 10) or klst < 8):
            return [["Degi lokið", 1, [18, 40, 8, 10], 7, 0]]
        for x in self.query:
            flag = False
            flag2 = True
            fra, til = x[2].split(":"), x[3].split(":")
            if (klst == 9 and 10 < minu < 15) or \
               (klst == 9 and 10 < minu < 15) or \
               (klst == 10 and 15 < minu < 35) or \
               (klst == 11 and 35 < minu < 40) or \
               ((klst == 12 and 40 < minu) or (klst == 13 and minu < 10)) or \
               (klst == 14 and 10 < minu < 15) or \
               (klst == 15 and 15 < minu < 30) or \
               (klst == 16 and 30 < minu < 35) or \
               (klst == 17 and 35 < minu < 40):
                flag2 = False
                return self.pasa

            if flag2:
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
