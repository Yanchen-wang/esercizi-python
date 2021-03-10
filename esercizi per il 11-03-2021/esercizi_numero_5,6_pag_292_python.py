'''
Elenca proprietà e metodi della classe prodotto.
Definisci il metodo assegna_prezzo della classe prodotto.
'''
n = 0

class Prodotto():
    def __init__(self, nome, materiale, prezzo):
        self.materiale = materiale

    def assegna_nome(self):
        self.nome = nome
        return nome

    def assegna_prezzo(self):
        self.prezzo = prezzo
        return prezzo

while True:
    try:
        n += 1
        print("inserire il nome del prodotto",n)
        nome = input()
        print("inserire il materiale del prodotto",n)
        materiale = input()
        print("inserire il prezzo del prodotto",n,"in euro")
        prezzo = float(input())
        prodotto_1 = Prodotto(nome, materiale, prezzo)
        costo = prodotto_1.assegna_prezzo()
        nome_prodotto_1 = prodotto_1.assegna_nome()
        print(nome_prodotto_1,"è fatto di", materiale,"e costa",costo,"euro")

        trigger = input("inserire 0 per riavviare il programma, inserire qualsisasi altra cosa per interromperlo")
        if trigger != "0":
            break
    except ValueError:
        n -= 1
        print("\nUNEXPECTED VALUE HAS BEEN INSERTED PLS ENTER A VALUE THAT CAN BE CONVERTED INTO AN INTEGER\n")
        continue