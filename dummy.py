with open("lausarstofur.csv", "r") as skra:
    asd = skra.read()
    listi = asd.split(";")
teljari = 0
for x in listi:
    if teljari % 5 == 0:
        print()
    print(x, end=" ")
    teljari += 1
"""
for x in range(len(listi)):
    if x == 500:
        break
    if x % 5 == 0:
        print("")
    print(listi[x], end=" ")
"""