Preise = {
	"Apfel": "0.60",
	"Banane": "0.40",
	"Orange": "0.70"
}

print("Preis Apfel: ", Preise["Apfel"])

Preise["Kiwi"] = 0.2

Preise["Apfel"] = 1.0

del Preise["Orange"]
print("Apfel" in Preise, "Kirsche" in Preise)

def get_total_price(Dict_Input):
	Output = 0
	for value in Dict_Input.values():
		Output += float(value)
	return Output
print(round(get_total_price(Preise), 2))

def get_lowest_price(Dict_Input):
	lower_price = float(100)
	for value in Dict_Input.values():
		if float(value) < lower_price:
			lower_price = float(value)
		else:
			pass
	return lower_price
print(round(get_lowest_price(Preise), 2))
