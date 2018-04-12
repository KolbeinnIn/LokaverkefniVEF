import sqlite3

with sqlite3.connect("stofur.db") as db:
    cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stofur(
        ID integer primary key,
        nafn VARCHAR(30) NOT NULL
    );
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS dagar(
        ID integer primary key AUTOINCREMENT,
        nafn VARCHAR(13) NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS timar(
        ID integer primary key AUTOINCREMENT,
        timi_fra CHAR(5) NOT NULL,
        timi_til CHAR(5) NOT NULL,
        stofur_ID integer NOT NULL, 
        dagar_ID integer NOT NULL,
        FOREIGN KEY (stofur_ID) REFERENCES stofur(ID),
        FOREIGN KEY (dagar_ID) REFERENCES dagar(ID)
    );
""")

cursor.execute("""
    INSERT INTO dagar(nafn)
    VALUES
        ("Mánudagur"),
        ("Þriðjudagur"),
        ("Miðvikudagur"),
        ("Fimmtudagur"),
        ("Föstudagur"),
        ("Laugardagur"),
        ("Sunnudagur")
""")
db.commit()
