parole = []
while True:
    parola = input("inserisci delle parole una alla volta ,quando hai finito inserisci 0")
    if parola != "0":
        parole.append(parola)
    else:
        break
print("le lunghezze delle parole sono rispettivamente di:")
for i in parole:
    print(len(i),"caratteri")