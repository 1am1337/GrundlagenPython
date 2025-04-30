floatValue = 1.0
intValue = 1
boolValue = True
stringValue = "Hello World!"
listExample = [floatValue, intValue, boolValue, stringValue] 	# veränderbar
tupleExample = (floatValue, intValue, boolValue, stringValue) 	# unveränderbar
dictionaryExample = {"float": floatValue,						# veränderbar
					"int": intValue,
					"bool": boolValue,
					"string": stringValue}
setExample = {1, 2, 3, 4, 5, 5}									# unveränderbar, aber neu einträge möglich
print(stringValue[::2]) 										#alle 2 stellen
print(stringValue[::-1]) 										#rückwärts
print(listExample.append("kein Output"), listExample + ["OUTPUT!!!! yay :)"])