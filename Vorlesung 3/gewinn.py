# Eingabe
umsatz = float(input("Umsatz: "))
kosten = float(input("Kosten: "))
# Achtung: input()-Funktion liefert als Ergebnis einen Typ <str>

# Alternative für Typumwandlung für oben
# umsatz = input("Umsatz")
# umsatz = float(umsatz)

# Verarbeitung
gewinn = umsatz - kosten

# Ausgabe
print(f"Der Gewinn ist: {gewinn:8.2f}") # 8 Stellen insgesamt, 2 Nachkommastellen
