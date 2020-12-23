'''
Fornisci la rappresentazione in binario di un numero decimale. Dopo aver acquisito 
il valore del Numero da trasformare, si esegue la divisione del numero per 2 e si 
calcola quoziente e resto. Il resto é la prima cifra della rappresentazione 
binaria. Si ripete il procedimento assegnando il quoziente ottenuto a Numero e 
ricalcolando la divisione per 2; la ripetizione prosegue mentre il quoziente 
ottenuto si mantiene diverso da zero. La rappresentazione binaria del numero 
decimale è costituita dalle cifre binarie ottenute come resti, lette in ordine 
inverso. Confronta poi il risultato con il valore ottenuto dalla funzione 
predefinita del linguaggio per convertire un numero decimale in binario. 
'''
resto = ""
while True:
    try:
        Numero = int(input("Scrivere il numero decimale da trasformare in binario:"))
        numero_binario = bin(Numero)
        break
    except ValueError:
        print("\nE' STATO INSERITO UN VALORE INASPETTATO, INSERIRE UN VALORE CONVERTIBILE IN INTEGER\n")
        pass
while Numero > 0:
    resto += str(Numero % 2)
    Numero = Numero//2
print("Il numero in binario risulta essere:", resto[::-1] ,",invece con la funzione di python risulta essere", numero_binario)