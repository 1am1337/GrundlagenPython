def dictionaries():

	# Bestehen aus Schlüssel-Werte-Paaren

	dictionary = { 'key0': 'value0', 'key1': 1 }
	dictionary['key2'] = 'value2'

	# Mittels des Schlüssels können wir Werte aus dem Dictionary auslesen.
	print(dictionary['key0'])
	print(dictionary['key1'])
	print(dictionary['key2'])
	print(dictionary)

#dictionaries()


## Nachtrag zum Öffnen von Dateien:
# Ist gefährlich, da Fehler im Programm die Datei korrumpieren koennen.
# Deshalb ist es sinnvoll, die offene Datei (innerhalb des with-Blocks) nur auszulesen und wieder zu schließen
# Kommt aber alles noch in GdP.

entire_file = "" # Sollte außerhalb des Scopes des with-Blocks existieren.
with open("mat.txt") as file:
	entire_file = file.read() # Mehr als diese Zeile hat in diesem with-Block nichts verloren.
# Und jetzt können wir mit dem String weiter arbeiten ohne uns Sorgen um die Integrität unserer Datei machen zu müssen.

# Konvertieren wir den mehrzeiligen String zu einer Liste von Strings!
# Jedes Element der Liste entspricht einer Zeile der eingelesenen Datei.
lines = entire_file.split("\n")

dictionary = {}

for line in lines:
	# Wir nehmen an, dass alle interessanten Konstanten vor der ersten [Section] auftreten.
	# Alles ab dem erster [-Zeichen interessiert also nicht.
	if line.startswith("["):
		break

	if line.find("#") != -1: # Strip comments. Gibt line.find() -1 zurück, gibt es in der Zeile kein #-Zeichen.
		if False: # Gerne True mit False ersetzen, um stattdessen den zweiten Ansatz auszuprobieren.
			line = line.split("#")[0]
			# Angenommen in unserer Zeile steht folgendes: 'Daten die uns interessieren # Kommentar # der uns nicht interessiert'.
			# split("#") gibt folgende Liste zurück: ['Daten die uns interessieren ', ' Kommentar ', 'der uns nicht interessiert'].
			# Und aus dieser Liste interessiert uns ja nur das erste Element aka der String bis zum ersten #-Zeichen.
			# In diesem Beispiel könnte man noch 'Daten die uns interessieren '.strip() Whitespaces entfernen.
		else:
			line = line[:line.find("#")]
			# line.find (weil != -1 schon ausgeschlossen) gibt uns die Stelle zurück, wo das "#" erstmals auftritt.
			# Damit können wir uns den String bis vor diesem "#" an der Stelle n zurückgeben lassen.
			# Dieser Ansatz drückt unsere Intention, den Rest der Zeile ab "#" zu verwerfen, besser aus als der vorige.
		line = line.strip()
			

	if line == "": # Wir ignorieren leere Zeilen. Und solche, die nur Kommentare enthalten haben: Die haben wir im vorigen Schritt ja entfernt.
		continue

	line = line.lower()

	if line.startswith("<"): # String-Konstanten
		pair = line.lstrip("<").split(">")
		dictionary[pair[0]] = pair[1] # Wir benutzen den Konstantennamen aus der Datei als Schlüssel.
		continue

	if line.startswith("{"): # Float-Konstanten
		pair = line.lstrip("{").split("}")
		dictionary[pair[0]] = float(pair[1])
		continue

print(dictionary)
