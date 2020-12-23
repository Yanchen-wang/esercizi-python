'''
Dato un elenco di studenti partecipanti a una gara sportiva di lancio del peso
(nome studente, lancio)visualizza il valore del lancio del vincitore.
'''
n = 1
elenco_risultati = []
partecipante = "b"
while partecipante != "" :
    try:       
        print("inserire i nomi dei studenti con il loro risultato in metri(inserire nulla per indicare la fine dell'elenco)")
        print("inserire nome candidato ",n)
        partecipante = input()
        print("inserire il risultato ottenuto dal candidato ",n)
        risultato = int(input())
        elenco_risultati.append(risultato)
        n += 1
    except ValueError:
        print("\nE' STATO INSERITO UN VALORE INCOMPATIBILE\n")
        pass
elenco_risultati.sort(reverse=True)
print("il vincitore ha ottenuto il risultato di",elenco_risultati[0],"metri")