# Problem bei Listen: Die Komplexität ist O(n)
telefonliste = [["Peter", "0152-98231155"],
                ["Jutta", "0171-8883211"],
                ["Kathrin", "0152-99966311"],
                ["Guido", "0177-1155669912"]]

telefonliste.append(["Jochen", "0161-39873231"])
telefonliste.append(["Lionel", "0178-99912331"])

for eintrag in telefonliste:
    print(eintrag)
    if eintrag[0] == "Kathrin":
        print(f"Hurra, gefunden!! Die Nummer ist {eintrag[1]}")
