'''
verifica se un numero e' pari o dispari (un numero e' pari quando il suo resto della divisione intera per 2 e' uguale a 0).
'''
ciclo = "0"
while ciclo == "0":
    try:
        numero = int(input("inserisci un numero per verificare se e' pari o dispari\n"))
        if numero % 2 == 1:
            print(numero,"e' un numero dispari")
        else:
            print(numero,"e' un numero pari") 
        ciclo = input("se vuole continuare inserire 0 se vuole fermarsi inserire qualsiasi altra cosa\n")
    except ValueError:
        print("\nE' STATO INSERITO UN VALORE INCOMPATIBILE\n")
        pass