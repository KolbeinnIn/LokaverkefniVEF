CREATE TABLE snid(
	ID int AUTO_INCREMENT primary key,
	skoli VARCHAR(255) NOT NULL,
	timar VARCHAR(255) NOT NULL
);

CREATE TABLE stofur(
	ID int AUTO_INCREMENT primary key,
	stofuNr int,
	dagur CHAR(3) NOT NULL,
	python_timarN[0] VARCHAR(10),
	python_timarN[1] VARCHAR(10),
	python_timarN[2] VARCHAR(10),
	python_timarN[3] VARCHAR(10)
);


INSERT INTO snid(skoli,timar)
VALUES
	("Tækniskólinn", "08:10-10:15&10:35-12:40&13:10-15:15&15:30-17:35")

INSERT INTO stofa(stofuNr,dagur,timar)
VALUES
	(620, "MAN", 0,1,1,1),
	(620, "TRI", 1,0,1,0),
	(620, "MID", 1,1,0,0),
	(620, "FIM", 1,1,1,0),
	(620, "FOS", 1,0,0,0),
	(620, "LAU", 0,0,0,0),
	(620, "SUN", 0,0,0,0);
	
	
--format timar: 08:10-10:15&10:35-12:40&13:10-15:15&15:30-17:35
--format timar: 00:00-00:00&00:00	
	
	
--fra0810t1015 BOOLEAN NOT NULL,
--fra1035t1240 BOOLEAN NOT NULL,
--fra1310t1515 BOOLEAN NOT NULL,
--fra1530t1735 BOOLEAN NOT NULL