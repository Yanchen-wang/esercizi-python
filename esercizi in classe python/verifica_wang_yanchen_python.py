from spalla import Verifica
Verifica.firma("Wang Yanchen")

def es1():
    es = Verifica.inizia_esercizio(1)
    somma = 0

    for numero in es.dati:
        if numero < 509:
            somma += numero

    es.consegna(somma)

def es2():
    es = Verifica.inizia_esercizio(2)
    numero_parole = 0

    for parola in es.dati:
        if len(parola) > 5:
            numero_parole += 1

    es.consegna(numero_parole)

def es3():
    es = Verifica.inizia_esercizio(3)
    lista_consegna = []

    for numero in es.dati:
        if numero % 2 == 1 and numero > 5:
            lista_consegna.append(numero)

    es.consegna(lista_consegna)

def es4():
    es = Verifica.inizia_esercizio(4)
    lista_dati = es.dati
    lista_indici = []

    for numero in lista_dati:
        if numero > 0:
            lista_indici.append(lista_dati.index(numero))

        lista_dati[lista_dati.index(numero)] = ""

    es.consegna(lista_indici)

def es5():
    es = Verifica.inizia_esercizio(5)
    lista_parole_d = []

    for parole in es.dati:
        if parole[0] == "d" or parole[-1] == "d":
            lista_parole_d.append(parole)

    es.consegna(lista_parole_d)

def es6():
    es = Verifica.inizia_esercizio(6)
    valore_minimo = 35
    lista_numeri_consegna = []

    for numero in range(es.dati + 1):
        if numero >= valore_minimo and numero % 4 != 0:
            lista_numeri_consegna.append(numero)

    es.consegna(lista_numeri_consegna)

def es7():
    es = Verifica.inizia_esercizio(7)
    lista_parole = es.dati.split(" ")
    lista_parole_consegna = []

    for parola in lista_parole:
        if parola[0] != "e" and parola[0] != "d":
            lista_parole_consegna.append(parola)

    es.consegna(lista_parole_consegna)

#es1()
#es2()
#es3()
#es4()
#es5()
#es6()
#es7()