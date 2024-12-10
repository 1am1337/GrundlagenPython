Einkaufsliste = ["Maultaschen", "Hafermilch", "Eier", "Brot", "Müsli"] 								#Erstellt eine Liste einkaufsliste mit mindestens fünf verschiedenen Artikeln (als Strings).
Einkaufsliste[1] = "Sojamilch"																		#Artikel Ändern: Ändert den zweiten Artikel in der Liste in einen anderen Artikel. (Wennder zweite Artikel z. B. "Brot" ist, ändert ihn in "Reis".)
Einkaufsliste.pop(len(Einkaufsliste)-1)																#Artikel Entfernen: Entfernt den letzten Artikel aus der Liste. (-1 weil len() die gesamte länge angibt, pop aber bei 0 anfängt) POP gibt auch output fancy
for i in range(len(Einkaufsliste)):																	#Liste Anzeigen: Verwendet eine for-Schleife, um über die Liste zu iterieren und jeden Artikel auszugeben.
	print("Eintrag", i+1, ":", Einkaufsliste[i])
print("Die Ersten Drei Einträge:", Einkaufsliste[0], Einkaufsliste[1], Einkaufsliste[2])			#Tellbereich der Liste: Gebt die ersten drei Artikel der Liste aus.																				#Umgekehrte Ausgabe: Gebt mittels einer for-Schleife die Artikel der Liste in umgekehrter Reihenfolge aus.
for i in range(len(Einkaufsliste)):																	#Umgekehrte Ausgabe: Gebt mittels einer for-Schleife die Artikel der Liste in umgekehrter Reihenfolge aus.
	print("Eintrag", len(Einkaufsliste)-i, ":", Einkaufsliste[i-len(Einkaufsliste)])
