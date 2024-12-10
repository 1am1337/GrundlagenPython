einkaufsliste2 = ["i1","i2","i3","i4","i5"]
#for elem in einkaufsliste2:
#	print(elem)

def aufgabe1(p_liste):
	lokale_liste = p_liste[:]
	lokale_liste[1] = "i2_new"
	return lokale_liste
print(einkaufsliste2)
print(aufgabe1(einkaufsliste2))
print(einkaufsliste2)
