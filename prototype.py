import sqlite3

with sqlite3.connect("proto.db") as db:
    cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS snid(
        ID integer AUTO_INCREMENT primary key,
        skoli VARCHAR(255) NOT NULL,
        timar VARCHAR(255) NOT NULL
    );
""")
cursor.execute("""
    INSERT INTO snid(skoli,timar)
    VALUES("Tækniskólinn", "08:10-10:15&10:35-12:40&13:10-15:15&15:30-17:35");
""")

"""
timar = "08:10-10:15&10:35-12:40&13:10-15:15&15:30-17:35"

print(timarN)
"""


def time():
    cursor.execute("SELECT timar FROM snid")
    timar = cursor.fetchall()
    return timar


for x in time():
    print(x)
print(time())
timarN = time()[0][0].split("&")
print(timarN)

stofur = ("""
    CREATE TABLE IF NOT EXISTS stofur(
        ID int AUTO_INCREMENT primary key,
        stofuNr int,
        dagur CHAR(3) NOT NULL,
        %s
    );
""")
timarNN = []
for x in timarN:
    asd = "f" + x.replace("-", "t")
    asd = asd.replace(":", "")
    timarNN.append(asd)
print(timarNN)
fjTima = 4
stuff = """"""

for x in range(fjTima):
    stuff += str(timarNN[0] + " integer,\n        ")

a = stofur % stuff

print(a)
# cursor.execute(a)

