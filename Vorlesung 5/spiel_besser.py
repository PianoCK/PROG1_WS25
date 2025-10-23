# Lustiges Zahlenratespiel
import random # Modul für Zufallszahlen
random.shuffle

# Hilfsvariable für richtige Tipps
anzahl_richtig = 0
anzahl_runden = 3

for runde in range(1,anzahl_runden + 1):
    print(f"\nRunde {runde}!")
    print("---------------------")
    zahl1 = random.randint(1,10)
    zahl2 = random.randint(1,10)
    ergebnis = zahl1 + zahl2

    print(f"Was ist {zahl1} + {zahl2} ?")
    tipp = float(input("Dein Tipp? "))

    if tipp == ergebnis:
        print("Toll. Richtig geraten!")
        anzahl_richtig += 1
    else:
        print(f"Das war leider falsch. {zahl1} + {zahl2} = {ergebnis}")

print(f"Du hast {anzahl_richtig}x richtig geraten.")