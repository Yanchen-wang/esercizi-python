from spalla import Verifica

Verifica.firma("Yanchen Wang")

def es1():
    es = Verifica.inizia_esercizio(1)
    print(es)
    somma = 0
    for i in range(len(es.dati)):
        if es.dati[i] > es.dati[0]:
            somma += es.dati[i]
    es.consegna(somma)
    
def es2():
    es = Verifica.inizia_esercizio(2)
    print(es)
    n = 0
    for i in range(len(es.dati)):
        if len(es.dati[i]) > 4:
            n += 1
    es.consegna(n)
    
def es3():
    es = Verifica.inizia_esercizio(3)
    print(es)
    lista_2 = []
    for i in es.dati:
        if i % 2 == 1 and i > 1:
            lista_2.append(i)
    es.consegna(lista_2)
    
def es4():
    es = Verifica.inizia_esercizio(4)
    print(es)
    lista_2 = []
    for i in range(len(es.dati)):
        if es.dati[i] < 0:
            lista_2.append(i)
    es.consegna(lista_2)

def es5():
    es = Verifica.inizia_esercizio(5)
    print(es)
    lista = []
    for i in range(len(es.dati["frutta"])):
        lista.append(es.dati["frutta"][i])
    print(lista)
    
def es6():
    es = Verifica.inizia_esercizio(6)
    print(es)
    lista = []
    for i in range(es.dati + 1):
        lista.append(i)
    lista.sort(reverse = True)
    es.consegna(lista)

def es7():
    es = Verifica.inizia_esercizio(7)
    print(es)
    lista = []
    for i in es.dati.split(" "):
        if i[0] == "e" or i[0] == "a":
            lista.append(i)
    es.consegna(lista)

#es1()
#es2()
#es3()
#es4()
es5()
#es6()
#es7()