listcandidati = [] 
listvoti = []
candidato1 = input("inserire il nome del primo candidato")
candidato2 = input("inserire il nome del secondo candidato")
print("inserire il numero di voti ottenuti da",candidato1)
voti1 = int(input())
print("inserire il numero di voti ottenuti da",candidato2)
voti2 = int(input())
listcandidati.append(candidato1) , listcandidati.append(candidato2)
listvoti.append(voti1) 
listcandidati.sort() 
print("lista candidati in ordine alfabetico:")
for l in listcandidati:
    print(l)
print("lista dei candidati per voti ottenuti ")
if voti1 > voti2:
    print(candidato1)
    print(candidato2)
else :
    print(candidato2)
    print(candidato1)