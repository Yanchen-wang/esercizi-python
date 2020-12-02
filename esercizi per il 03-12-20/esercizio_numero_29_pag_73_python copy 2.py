conteggio_città_selezionate = 0
città_ = 0
n = 1
escursione_prefissta = int(input("inserire il valore prefissato dell'escursione termica in gradi celsius"))
while True:
    try:
        print("inserire il nome della città numero",n,"inserire nulla per indicare la fine dell'elenco")
        città_ = input()       
        if città_ != "":        
            temperatura_massima = int(input("inserire la temperatura massima giornaliera raggiunta in gradi celsius"))
            temperatura_minima = int(input("inserire la temperatura minima giornaliera raggiunta in gradi celsius"))       
            if temperatura_massima < temperatura_minima:
                print("\nErrore valore massimo risulta minore del valore minimo, rinserire dati\n")
            elif temperatura_massima-temperatura_minima > escursione_prefissta: 
                conteggio_città_selezionate += 1
                n += 1
            else:
                n += 1        
        else:
            break
    except ValueError:
        print("\nE' STATO INSERITO VALORE INCOMPATIBILE\n")
        pass
print("il numero delle città registrate nel contatore sono",conteggio_città_selezionate)