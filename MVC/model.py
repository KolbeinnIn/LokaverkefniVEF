# Kolbeinn Ingólfsson
# Verkefni 4 - VEFII
# Model
import sqlite3
import time

with sqlite3.connect("../stofur.db") as db:
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
b = cursor.execute("""SELECT *
                      FROM bygging;""")

byggingar = cursor.fetchall()



class Laust:
    def __init__(self, query):
        self.query = query
        self.nyr = []
        
    def current_time(self):
        klukk = get_time()[3]
        minu = get_time()[4]
        current_dagur = get_time()[6]
        for x in self.query:
            fra, til = x[2].split(":"), x[3].split(":")
            timi = [x[0], x[1], [int(fra[0]), int(fra[1]), int(til[0]), int(til[1])], x[4], x[5]]
            if timi[2][2] >= klukk >= timi[2][0] and x[4] == current_dagur:
                if minu >= timi[2][1]:
                    self.nyr.append(timi)
        return self.nyr
    
    def selected_time(self, klst, minu, day):
        for x in self.query:
            fra, til = x[2].split(":"), x[3].split(":")
            timi = [x[0], x[1], [int(fra[0]), int(fra[1]), int(til[0]), int(til[1])], x[4], x[5]]
            if timi[2][2] >= klst >= timi[2][0]:
                if minu <= timi[2][3] and klst == timi[2][2]:
                    self.nyr.append(timi)

            if timi[2][2] >= klst == timi[2][0] and minu >= timi[2][1]:
                self.nyr.append(timi)
        return self.nyr



# print(get_time()[3], get_time()[4])


def activate(klasi, b_listi):
    bygging = "Óvitað"
    for x in klasi:
        if x[-1] == 1:
            bygging = b_listi[0][1]
        elif x[-1] == 2:
            bygging = b_listi[1][1]
        elif x[-1] == 3:
            bygging = b_listi[2][1]

        print("Stofa %s er laus frá kl %d:%d - %d:%d\n"
              "Bygging: %s\n" % (x[0], x[2][0], x[2][1], x[2][2], x[2][3], bygging))


#activate(selected, byggingar)
#activate(current, byggingar)

