# Lustiges Zahlenratespiel
import random # Modul für Zufallszahlen
random.shuffle

zahl1 = random.randint(1,10)
zahl2 = random.randint(1,10)
ergebnis = zahl1 + zahl2

print(f"Was ist {zahl1} + {zahl2} ?")
tipp = float(input("Dein Tipp? "))

if tipp == ergebnis:
    print("Toll. Richtig geraten!")
else:
    print(f"Das war leider falsch. {zahl1} + {zahl2} = {ergebnis}")

