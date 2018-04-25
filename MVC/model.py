# Kolbeinn Ingólfsson
# Verkefni 4 - VEFII
# Model
import sqlite3
import time

with sqlite3.connect("stofur.db") as db:
    cursor = db.cursor()


def get_time():
    now = time.localtime()
    return now


b = cursor.execute("SELECT * FROM timar limit(10)")
listi = cursor.fetchall()
#print(listi)

#                         b
# (auto id, timi_fra, timi_til, stofur_ID, dagur_ID
# (1,       '08:10',  '08:50',     1,          1)

dagar = ["mánudagur",
         "þriðjudagur",
         "miðvikudagur",
         "fimmtudagur",
         "föstudagur",
         "laugardagur",
         "sunnudagur"]


class Timar:
    def __init__(self, listinn):
        self.listi = listinn

    def query(self, timi):
        listi2 = []
        a = cursor.execute("""SELECT stofur.nafn, timar.timi_fra, timar.timi_til
                           FROM stofur, timar
                           WHERE stofur.ID = timar.stofur_ID
                           LIMIT(10);""")
        a1 = cursor.fetchall()
        for x in a1:
            fra = x[1].split(":")

        return listi2

    def timi(self):
        return self.listi


timar = Timar(listi).timi()
# q = Timar(listi).query("11:25")


#
timi = "11:25"

a = cursor.execute("""SELECT stofur.nafn, stofur.ID, timar.timi_fra, timar.timi_til, timar.dagar_ID
                       FROM stofur, timar
                       WHERE stofur.ID = timar.stofur_ID
                       limit(100);""")

a1 = cursor.fetchall()
nyr = []
for x in a1:
    fra, til = x[2].split(":"), x[3].split(":")
    timi2 = [x[0], x[1], [int(fra[0]), int(fra[1]), int(til[0]), int(til[1])], x[-1]]
    if timi2[2][2] > get_time()[3] == timi2[2][0]:
        print(timi2)
        nyr.append(timi2)
print(get_time()[3], get_time()[4])







