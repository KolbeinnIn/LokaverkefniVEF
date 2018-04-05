# Kolbeinn Ingólfsson
# Dummy file til að testa bunch að kóða


listi2 = []
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
for x in range(0, len(listi2), 5):
    lyklar.append(listi2[x])
    dicta = {listi2[x]: [listi2[x + 1], listi2[x + 2], listi2[x + 3], listi2[x + 4]]}
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
    # print(listi2[x], end=" ")

man2 = []
tri2 = []
mid2 = []
fim2 = []
fos2 = []
lau2 = []
temp = []





