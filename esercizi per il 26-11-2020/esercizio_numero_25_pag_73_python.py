'''
A un concorso pubblico hanno partecipato due candidati di cui si conoscono i nomi
e i punteggi conseguiti. Visualizza l'elenco dei due candidati prima in ordine
alfabetico e poi in ordine di punteggio.
'''
listcandidati = [] 
listvoti = []
candidato1 = input("inserire il nome del primo candidato")
candidato2 = input("inserire il nome del secondo candidato")
print("inserire il numero di voti ottenuti da",candidato1)
while True:
    try:
        voti1 = int(input())
        print("inserire il numero di voti ottenuti da",candidato2)
        voti2 = int(input())
        listcandidati.append(candidato1) , listcandidati.append(candidato2)
        break
    except ValueError:
        print("\nUNEXPECTED VALUE HAS BEEN INSERTED PLS ENTER A VALUE THAT CAN BE CONVERTED INTO AN INTEGER\n")
        pass
listcandidati.sort() 
print("lista candidati in ordine alfabetico:")
for l in listcandidati:
    print(l)
print("lista dei candidati per voti ottenuti:")
if voti1 > voti2:
    print(candidato1)
    print(candidato2)
elif voti1 == voti2:
    print("pareggio")
else:
    print(candidato2)
    print(candidato1)
