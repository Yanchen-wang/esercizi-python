'''
I dati relativi al numero di veicoli transitati in entrata a un casello
autostradale sono inseriti, giorno per giorno, con una ripetizione che termina
quando si inserisce 0 come segnalazione della fine dell'input dei dati. Comunica
il totale dei veicoli transitati nel periodo considerato.
'''
veicoli_giornalieri = -1
veicoli_totali = 0 
while veicoli_giornalieri != 0:
    try:
        print("inserire il numero dei veicoli transitati in ciascun giorno del periodo considerato per l'entrata del casello dell'autostrada,inserire 0 per indicare il termine del periodo considerato")
        veicoli_giornalieri = int(input())
        veicoli_totali += veicoli_giornalieri
    except ValueError:
        print("\nUNEXPECTED VALUE HAS BEEN INSERTED PLS ENTER A VALUE THAT CAN BE CONVERTED INTO AN INTEGER\n")
        pass
print("in tutto",veicoli_totali,"veicoli sono transitati durante periodo considerato")