numeri = []
somma_numeri = 0
coefficente_potenza = 0
n = 0
valore_binario = ""
lunghezza_binaria = int(input("Inserire la lunghezza del numero binario"))
for l in range(lunghezza_binaria):
    n += 1
    print("A partire da destra inserire la cifra numero", n)
    cifra = int(input())
    numeri.append(cifra)   
numeri.reverse()
print("Il numero binario diviso in cifre singole risulta essere: ",numeri)
for l in range(lunghezza_binaria):
    cifra_binaria = numeri[lunghezza_binaria-1]
    valore_binario = str(cifra_binaria) + valore_binario
    if cifra_binaria == 1:
        somma_numeri += 2**coefficente_potenza
    lunghezza_binaria -= 1
    coefficente_potenza += 1
print("Il numero decimale ottenuto risulta essere: ",somma_numeri,"mentre la funzione di python restituisce",int(valore_binario, 2))