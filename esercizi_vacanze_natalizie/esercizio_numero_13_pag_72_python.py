'''
verifica se un numero e' pari o dispari (un numero e' pari quando il suo resto della divisione intera per 2 e' uguale a 0).
'''
numero = int(input("inserisci un numero per verificare se e' pari o dispari"))
if numero % 2 == 1:
    print(numero,"e' un numero dispari")
else:
    print(numero,"e' un numero pari")
