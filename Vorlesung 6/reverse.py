# Meine tolle reverse Funktion
def reverse(wort):
    wortlaenge = len(wort)
    neues_wort=""
    for index in range(wortlaenge-1,-1,-1):
        neues_wort += wort[index]
    return neues_wort

#              01234
print(reverse("LAGER"))