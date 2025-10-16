# Eingabe
wahl = input("(H)ier essen oder (N)achhausenehmen? ")

if wahl == "h" or wahl == "H":
    print("7% Mehrwertsteuer")
    print("Dankeschön")
elif wahl == "n" or wahl == "N":
    print("19% Mehrwertsteuer")
    print("Mist. Ich verdiene weniger Geld.")
else:
    print("Fehleingabe")

print("Fertig.")

