
while True:
    zahl = input("Bitte gib eine Zahl ein: ")
    try:
        zahl = int(zahl)
        break
    except:
        print(f"Fehler. Bitte nochmal versuchen.")

print(f"Deine Zahl ist {zahl}")