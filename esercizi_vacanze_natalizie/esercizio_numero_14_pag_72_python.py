'''
Crea un programma che scriva l differenza di due numeri a e b se il loro prodotto e' maggiore di 10 oppure la loro somma
se il prodotto e' minore o uguale a 10. Esegui poi il programma con diverse coppie di valori per a e b: (-5, 2),(5,-5),
(10, 2),(-4,-5),(5, 4),(-3,-2).
'''
ciclo = "0"
while ciclo == "0":
    try:
        a = int(input("inserire il valore del numero a"))
        b = int(input("inserire il valore del numero b"))
        if a * b > 10:
            print("la differenza tra a e b e':",a - b)
        else:
            print("la somma tra a e b e':",a + b)
        ciclo = input("se vuole continuare inserire 0 se vuole fermarsi inserire qualsiasi altro valore")
    except ValueError:
        print("\nE' STATO INSERITO UN VALORE INCOMPATIBILE\n")
        pass