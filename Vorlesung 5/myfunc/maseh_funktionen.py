def maseh_add2_orig(irgendeine_zahl):
    '''  Diese Maseh-Funktion nimmt eine Integer-Zahl und gibt die Zahl+2 zurück.
    '''
    return irgendeine_zahl + 2

def maseh_add2(irgendeine_zahl: int) -> int:
    '''  Diese Maseh-Funktion nimmt eine Integer-Zahl und gibt die Zahl+2 zurück.
    '''
    print("\nHallo, ich bin Maseh und rechne für dich.")
    print(f"Aha, ich sehe, Du hast mir eine {irgendeine_zahl} gegeben.")
    print("Lass mich rechnen...")
    ergebnis = irgendeine_zahl + 2
    print(f"Ich bin fertig mit rechnen. Das Ergebnis ist {ergebnis}.")
    return ergebnis

def maseh_add2_mit_print(zahl):
    print(f"Ich gebe der Funktion eine {zahl} und mase_add2 sagt {maseh_add2(zahl)}")

maseh_add2_mit_print(-2)
maseh_add2_mit_print(5)
maseh_add2_mit_print(10)