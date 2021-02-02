'''
in un laboratorio di analisi i pazienti sono sottoposti ad esame secondo l'ordine di arrivo (usa una struttura di coda per
memorizzare i nomi): srivi il programma che registri i nomi dei pazienti man mano che arrivano. visualizza poi il primo
paziente che deve essere sottoposto all'esame.
'''
coda = []
while True:
    paziente = input("inserire il nome del paziente che e' arrivato, inserire nulla per indicare che non ci sono piu' pazienti")
    if paziente == "":
        break
    coda.append(paziente)
print("il nome del paziente che deve essere sottoposto all'esame e'", coda[0])