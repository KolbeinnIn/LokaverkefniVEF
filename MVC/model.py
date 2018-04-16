# Kolbeinn Ingólfsson
# Verkefni 4 - VEFII
# Model
import sqlite3
import time

dicta = {"Robert Downey Jr.": [52, "1.74 m", "The lesson is that you can still make mistakes and be forgiven."],
         "Chris Evans": [36, "1.83 m", "But my happiness in this world - my level of peace - is never going to be dictated by acting."],
         "Chris Hemsworth": [34, "1.9 m", "For me, life is about experience and being a good person."],
         "Scarlett Johansson": [33, "1.6 m", "I hope they make a video game of me. At least I wouldn't have any cellulite then."],
         "Mark Ruffalo": [50, "1.73 m", "People say funny things all the time during really serious moments in life."],
         "Jeremy Renner": [47, "1.75 m", "I like repressed characters. That gives me a lot of freedom to make a lot of different choices through subtleties."],
         "Samuel L. Jackson": [69, "1.89 m", "Not everybody goes to movies to get their life changed."]
         }


class Leikari:
    def __init__(self, dictionary):
        self.dicta = dictionary

    def listi(self):
        return self.dicta


with sqlite3.connect("stofur.db") as db:
    cursor = db.cursor()


def get_time():
    now = time.localtime()
    return now


a = cursor.execute("""SELECT stofur.nafn, timar.timi_fra, timar.timi_til
                   FROM stofur, timar
                   WHERE stofur.ID = timar.stofur_ID
                   LIMIT(10);""")
a1 = cursor.fetchall()
#b = cursor.execute("SELECT * FROM timar WHERE ")
#b1 = cursor.fetchall()
print(a1)

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