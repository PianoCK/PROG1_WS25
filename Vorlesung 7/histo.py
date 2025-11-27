zahlen = "01937483020345474565069545972853127192345058743647392374094340984734509834309847632156234789"
# listenindex  0  1  2  3  4  5  6  7  8  9
zahlenliste = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Idee: Im Listenindex 3 steht die Anzahl der 3en

for zahl in zahlen:
    zahlenliste[int(zahl)] += 1    

for zahl in range(10):
    print(f"Von der Zahl {zahl} gibt es {zahlenliste[zahl]} Einträge")

