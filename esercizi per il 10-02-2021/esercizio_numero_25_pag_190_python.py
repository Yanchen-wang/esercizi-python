'''
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionario che ha per chiave
la matricola, mentre il valore associato e' il voto. Elenca i risultati in ordine crescente di voto e successivamente 
visulizza quali voti diversi tra loro sono stati assegnati, riducendo a uno i voti uguali.
'''
dizionario_voti = {}
lista_voti = []
lista_voti_unici = []

for studenti in range(30):
    
    while True:
        try:
            print("inserire la matricola dello studente numero", studenti + 1)
            matricola = input()
            if matricola in dizionario_voti:
                voto = "a"
                print("la matricola e' gia stata inserita")
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
            pass 

for voti in dizionario_voti:
    lista_voti.append(dizionario_voti[voti])
lista_voti_crescenti = sorted(lista_voti)

print("i voti in ordine crescente sono:",lista_voti_crescenti)

for voti in lista_voti:
    if voti not in lista_voti_unici:
       lista_voti_unici.append(voti)
print("i voti che sono stati assegnati sono:",lista_voti_unici)