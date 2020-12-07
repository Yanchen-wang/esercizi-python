parole = []
while True:
    parola = input("inserisci di continuo delle parole ,quando hai finito inserisci inserisci nulla")
    if parola != "":
        parole.append(parola)
    else:
        break
print("le lunghezze delle parole sono rispettivamente:")
for i in parole:
    print(len(i))