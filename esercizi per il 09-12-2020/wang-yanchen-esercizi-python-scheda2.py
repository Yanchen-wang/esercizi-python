'''
Scrivi una programma che data in ingresso una lista A contenente n parole, 
restituisca in output una lista B di interi che rappresentano la lunghezza 
delle parole contenute in A. 
'''
parole = []
lunghezze_parole = []
while True:
    parola = input("inserisci delle parole una alla volta ,quando hai finito inserisci 0")
    if parola != "0":
        parole.append(parola)
    else:
        break
print("le lunghezze delle parole sono rispettivamente di:")
for i in parole:
    lunghezze_parole.append(len(i))
print(lunghezze_parole)    