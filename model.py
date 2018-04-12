# Kolbeinn Ingólfsson
# Model fyrir lokaverkefni vef
# Sér um að taka upplýsingarnar úr database-inu.

import sqlite3
import time


with sqlite3.connect("stofur.db") as db:
    cursor = db.cursor()


def get_time():
    now = time.localtime()
    return now


a = cursor.execute("SELECT * FROM timar")
a1 = cursor.fetchall()
b = cursor.execute("SELECT * FROM timar WHERE timi_fra = '08:10' AND dagar_ID = 6;")
b1 = cursor.fetchall()
print(a1)
print(b1)

dagar = ["mánudagur",
         "þriðjudagur",
         "miðvikudagur",
         "fimmtudagur",
         "föstudagur",
         "laugardagur",
         "sunnudagur"]

teljari = 1
print("Í dag er " + str(dagar[get_time()[6]]) + ".\nMánaðardagur: " + str(get_time()[2]) + "/" + str(get_time()[1]))
if get_time()[4] > 9:
    print("klukkan er: %s:%s" % (get_time()[3], get_time()[4]))
else:
    print("klukkan er: %s:0%s" % (get_time()[3], get_time()[4]))


