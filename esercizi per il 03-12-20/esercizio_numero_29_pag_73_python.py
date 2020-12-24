'''
Dato un elenco di città, con l'indicazione per ciascuna di esse del nome e delle temperature massima e minima registrate
in un giorno, si devono contare quante città hanno superato nel giorno un valore prefissato per l'escursione termica, 
ottenuta per differenza tra temperatura massima e minima. Organizza un programma che, dopo aver richiesto il valore da 
controllare dell'escursione termica, per ogni città dell'elenco ripeta la richiesta dei dati (nome, temperatura massima e 
minima), calcoli l'escursione termica e controlli se l'escursione è maggiore del valore prefissato: in questo caso,
incrementa il contatore delle città selezionate. Alla fine della ripetizione comunica il numero delle città registrato 
nel contatore.
'''
conteggio_citta_selezionate = 0
citta_ = 0
n = 1
escursione_prefissta = int(input("inserire il valore prefissato dell'escursione termica in gradi celsius"))
while True:
    try:
        print("inserire il nome della città numero",n,"inserire nulla per indicare la fine dell'elenco")
        citta_ = input()       
        if citta_ != "":        
            temperatura_massima = int(input("inserire la temperatura massima giornaliera raggiunta in gradi celsius"))
            temperatura_minima = int(input("inserire la temperatura minima giornaliera raggiunta in gradi celsius"))       
            if temperatura_massima < temperatura_minima:
                print("\nErrore valore massimo risulta minore del valore minimo, rinserire dati\n")
            elif temperatura_massima-temperatura_minima > escursione_prefissta: 
                conteggio_citta_selezionate += 1
                n += 1
            else:
                n += 1        
        else:
            break
    except ValueError:
        print("\nE' STATO INSERITO VALORE INCOMPATIBILE\n")
        pass
print("il numero delle città registrate nel contatore sono",conteggio_citta_selezionate)