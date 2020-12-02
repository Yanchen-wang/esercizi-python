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