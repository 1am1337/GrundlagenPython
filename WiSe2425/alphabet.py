import string
alphabet = []
for i in range(0,26):
    alphabet.append(string.ascii_lowercase[i])
for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        print(alphabet[i],alphabet[j], )