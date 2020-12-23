'''
Scrivi un programma a cui viene passata una parola e riconosce se si tratta di un
palindromo (parole che si leggono uguali anche al contrario) oppure meno.
'''
parola = input("inserire una parola")
alorap = parola[::-1]
if parola == alorap:
    print("la parola inserita è un palindromo")
else: 
    print("la parola inserita non è un palindromo")