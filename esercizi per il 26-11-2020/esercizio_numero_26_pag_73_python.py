'''
Calcola la media degli stipendi dei dipendenti di un'azienda, acquisiti con una
ripetizione fino a quando si inserisce il valore -1 per segnalare la fine 
dell'input dei dati.
'''
stipendo_individuo = 0
somma_stipendenti = 0 
numero_dipendenti = 0
while stipendo_individuo != -1:
    try:
        print("inserire lo stipendio di ciascun dipendente in euro,inserire -1 per terminare il processo ")
        stipendo_individuo = int(input())
        somma_stipendenti += stipendo_individuo
        numero_dipendenti += 1
    except ValueError:
        print("\nUNEXPECTED VALUE HAS BEEN INSERTED PLS ENTER A VALUE THAT CAN BE CONVERTED INTO AN INTEGER\n")
        pass
print("la media degli stipendi e' di",somma_stipendenti/numero_dipendenti,"euro")