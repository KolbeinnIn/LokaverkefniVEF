# Kolbeinn Ingólfsson
# Forrit sem tekur kóða frá csv skrá og vinnur úr henni go setur upplýsingarnar í gagnasafn


import sqlite3

listi2 = []
with sqlite3.connect("stofur.db") as db:
    cursor = db.cursor()

with open("lausarstofur.csv", "r", encoding="ISO-8859-1") as skra:
    asd = skra.read()
    listi = asd.split("\n")
for x in listi:
    a = x.split(";")
    for i in a:
        listi2.append(i)

lyklar = []
man = []
tri = []
mid = []
fim = []
fos = []
lau = []
teljari = 1
for x in range(0, len(listi2)-5, 5):
    if listi2[x] not in lyklar:
        lyklar.append([teljari, listi2[x]])
    dicta = {str(teljari) + ";" + listi2[x]: [listi2[x + 1], listi2[x + 2], listi2[x + 3], listi2[x + 4]]}
    teljari += 1
    if listi2[x + 2] == "1":
        man.append(dicta)
    elif listi2[x + 2] == "2":
        tri.append(dicta)
    elif listi2[x + 2] == "3":
        mid.append(dicta)
    elif listi2[x + 2] == "4":
        fim.append(dicta)
    elif listi2[x + 2] == "5":
        fos.append(dicta)
    elif listi2[x + 2] == "6":
        lau.append(dicta)

man2 = []
tri2 = []
mid2 = []
fim2 = []
fos2 = []
lau2 = []
temp = []

def lyklar2(y, listi_d):
    b = listi_d[y].keys()
    b = [l for l in b][0]
    return b


def stofur(key_listi):
    for x in key_listi:
        innsetning = ("""
            INSERT INTO stofur(ID, nafn)
            VALUES(%d, "%s")
        """) % (int(x[0]), str(x[1]))
        cursor.execute(innsetning)


def insert(dag_listi):
    global dagar_ID, timi_fra, timi_til
    for x in range(len(dag_listi)):
        for key, value in dag_listi[x].items():
            dagar_ID = value[1]
            timi_fra = value[2]
            timi_til = value[3]
        stofur_ID = lyklar2(x, dag_listi).split(";")[0]
        innsetning = ("""
            INSERT INTO timar(stofur_ID, dagar_ID, timi_fra, timi_til)
            VALUES(%d, %d, "%s", "%s")
        """) % (int(stofur_ID), int(dagar_ID), str(timi_fra), str(timi_til))
        cursor.execute(innsetning)


# stofur(lyklar)
insert(man)
insert(tri)
insert(mid)
insert(fim)
insert(fos)
insert(lau)
db.commit()
"""
#Killed hugmynd að hafa nafn á stofu sem key og safna öllum tímunum í lista sem value en það er smá erfitt so no...
for x in range(len(man)):
    def lyklar(y):
        if y-2 >= len(man):
            b = man[y].keys()
        else:
            b = man[y-2].keys()
        b = [l for l in b][0]
        return b


    if lyklar(x) == lyklar(x + 2):
        for i, value in man[x].items():
            if i not in temp:
                if lyklar(x) == lyklar(x + 1):
                    temp.append(i)
            if value[0] not in temp and value[1] not in temp:
                temp.append(value[0])
                temp.append(value[1])

            if value[2] not in temp and value[3] not in temp:
                temp.append(value[2])
                temp.append(value[3])
    else:
        man2.append(temp)
        temp = []
    print(lyklar(x+1), x)

del(man2[0])
print(man2)
"""
