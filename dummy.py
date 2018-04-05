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
    dagar = [listi2[x], listi2[x + 1], listi2[x + 2], listi2[x + 3], listi2[x + 4]]
    if listi2[x + 2] == "1":
        man.append(dagar)
    elif listi2[x + 2] == "2":
        tri.append(dagar)
    elif listi2[x + 2] == "3":
        mid.append(dagar)
    elif listi2[x + 2] == "4":
        fim.append(dagar)
    elif listi2[x + 2] == "5":
        fos.append(dagar)
    elif listi2[x + 2] == "6":
        lau.append(dagar)
    # print(listi2[x], end=" ")

man2 = []
tri2 = []
mid2 = []
fim2 = []
fos2 = []
lau2 = []
temp = []
for x in range(len(man)):
    print(man[x][0], man[x][1], man[x][2], man[x][3], man[x][4])
    if man[x][0] == man[x + 1][0]:
        for i in range(len(man)):
            if man[x][0] == man[x - 1][0]:
                temp = [man[x][0]]

    else:
        dummy = "dummy"
