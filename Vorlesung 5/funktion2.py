
# Aufgabe: Maseh Funktion "Hallo" + Wort

def maseh_hallo(irgendein_wort = "") -> str:
    ''' Diese Maseh-Funktion nimmt ein Wort und ergänzt "Hallo" + Wort
    '''
    print(f"Hallo {irgendein_wort}")
    return None # Das muss hier nicht sein, es ist Standard, wenn kein return angegeben wurde



maseh_hallo("Welt")
maseh_hallo(55)
maseh_hallo()