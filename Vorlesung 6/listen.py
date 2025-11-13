liste = []
liste.append("Einkaufen gehen")
liste.append("Python lernen")
liste.append("Sport machen")
liste.insert(0,"Geld abheben")
# del liste[3]    # Löschen am Listenindex 3
liste.remove("Sport machen") # wird nur der erste gefundene Eintrag gelöscht
eintrag = liste.pop(0) # Pop löscht den Eintrag und gibt den Eintrag als return zurück
liste.insert(3, eintrag)
print(liste)
