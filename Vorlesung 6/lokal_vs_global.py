PI = 3.14   # Globale Konstanten sind immer GROßGESCHRIEBEN

def a(x):
    x = x + PI  # Ich darf auf globale Variablen zugreifen, aber nicht ändern
    print("A")
    return x

# Hauptprogramm
x = 3
x = a(x)        # Call by Value (nicht Call by Reference!)
print(x)

