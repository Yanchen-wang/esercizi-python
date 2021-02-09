'''
Con riferimenti al dizionario del problema precedente, elenca i numeri di matricola degli studenti che hanno ottenuto una
votazione superiore alla media di tutte le votazioni.
'''
dizionario_voti = {}
lista_voti = []
lista_numero_matricola_studenti_superiori = []
posizioni_voti_superiori = []
lista_numeri_matricola = []

for studenti in range(30):
    while True:
        try:
            print("inserire il numero di matricola dello studente numero", studenti + 1)
            matricola = input()
            if matricola in dizionario_voti:
                voto = "a"
                print("il numero di matricola e' gia stato inserito")
                int(voto)
            print("inserire il voto di italiano di", matricola)
            voto = float(input())
            if voto > 10 or voto < 0:
                voto = "a"
                print("inserito un voto impossibile")
                int(voto)
            dizionario_voti[matricola] = voto
            break
        except ValueError:
            print("\nUNEXPECTED VALUE HAS BEEN INSERTED PLS ENTER A VALUE THAT CAN BE CONVERTED INTO AN INTEGER\n")
            continue

for voti in dizionario_voti:
    lista_voti.append(dizionario_voti[voti])

media_voti = (sum(lista_voti))/30

for numeri_matricola in dizionario_voti:
    lista_numeri_matricola.append(numeri_matricola)

for voti in lista_voti:
    if voti > media_voti:
        posizioni_voti_superiori.append(lista_voti.index(voti))
        lista_voti[lista_voti.index(voti)] = 0

for numeri_matricola in lista_numeri_matricola:
    if lista_numeri_matricola.index(numeri_matricola) in posizioni_voti_superiori:
        lista_numero_matricola_studenti_superiori.append(lista_numeri_matricola[lista_numeri_matricola.index(numeri_matricola)])
print(lista_numero_matricola_studenti_superiori)