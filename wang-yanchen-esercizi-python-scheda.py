parola = input("inserire una parola")
alorap = parola[::-1]
if parola == alorap:
    print("la parola inserita è un palindromo")
else: 
    print("la parola inserita non è un palindromo")