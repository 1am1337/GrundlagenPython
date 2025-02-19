import math

Preise = {
	"Apfel": 0.60,
	"Banane": 0.40,
	"Orange": 0.70
}

print("Preis Apfel: ", Preise["Apfel"])

Preise["Kiwi"] = 0.2

Preise["Apfel"] = 1.0

del Preise["Orange"]
print("Apfel" in Preise, "Kirsche" in Preise)

# def get_total_price(Dict_Input):
# 	Output = 0
# 	for value in Dict_Input.values():
# 		Output += value
# 	return Output
# print(get_lowest_price(Preise))
def get_total_price(fruits):
	total_price = 0
	for fruit in fruits:
		if fruit in Preise:
			total_price += Preise[fruit]
		else:
			print(f"{fruit} nicht in Dict")
	return total_price
print(get_total_price(["Apfel", "Banane", "TestError"]))


def get_lowest_price(Dict_Input):
	lower_price = math.inf								#sehr unprofessionell
	for value in Dict_Input.values():
		if float(value) < lower_price:
			lower_price = value
		else:
			pass
	return lower_price
print(get_lowest_price(Preise))

#oder:
# def get_value_for_key(key):
# 	return Preise[key]

# frucht_list = list(Preise.keys())
# frucht_list.sort(key = get_value_for_key)


# preis_list = list(Preise.values())
# preis_list.sort()
# print(frucht_list[0],":",preis_list[0])

#oder
min_val = 10000
min_item = ""
for fruit, price in Preise.items():
	if price < min_val:
		min_val = price 
		min_item = fruit
	else:
		pass
print(min_val, min_item)


