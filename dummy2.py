import sqlite3

with sqlite3.connect("dummyDB.db") as db:
    cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS stofur(
        ID integer primary key,
        nafn VARCHAR(30) NOT NULL
    )
    
    CREATE TABLE IF NOT EXISTS dagar(
        ID integer AUTOINCREMENT primary key,
        nafn VARCHAR(13) NOT NULL
    )
    
    CREATE TABLE IF NOT EXISTS timar(
        ID integer AUTOINCREMENT primary key,
        stofur_ID integer, 
        timi_fra CHAR(5) NOT NULL,
        timi_til CHAR(5) NOT NULL,
        dagar_ID integer,
        FOREIGN KEY (stofur_ID) REFERENCES stofur(ID),
        FOREIGN KEY (dagar_ID) REFERENCES dagar(ID)
    );
""")

cursor.execute("""
    INSERT INTO bygging(nafn, address)
    VALUES
        ('Vörðuskóli', 'Skólavörðuholt 101 Reykjavík'),
        ('Tækniskólinn aðalbygging', 'Skólavörðuholt 101 Reykjavík')
    
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

