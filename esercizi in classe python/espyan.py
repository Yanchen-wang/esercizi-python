'''
Si definisca una funzione che preso un dizionario di studenti e voti, restituisca un dizionario con gli studenti suddivisi
per intervalli di media di voto: k1 (18,23), k2(24,26) e k3(27,30). Nel calcolo della media la lode permette di arrotondare
all’intero successivo, nel caso in cui nella lista dei voti non sia presente una lode l’arrotondamento è per difetto.
'''
def main():
    stop = ""
    dizionario = {}
    dizionario_medie = {} 
    lista_nomi_a = []
    lista_nomi_b = []
    lista_nomi_c = []
    elenco_medie = {
        (18,23) : "",
        (24,26) : "",
        (27,30) : ""
    }

    while stop == "":
        
        try:
            n = 0
            voti = []
            nome = input("inserisci il nome dello studente\n").capitalize()

            while True:
                print("inserici il voto numero", n + 1,"di", nome ,", o inserire 0 quando non ci sono piu' voti")
                voto = int(input())
                if voto == 0 and n > 0:
                    break
                if voto == 0 and n == 0:
                    int("a")
                if voto > 30 or voto < 18 :
                    int("a")
                voti.append(voto)
                n += 1  
            
            dizionario[nome] = voti
            stop = input("se ci sono altri studenti inserire nulla, altrimenti inserire qualsiasi altra cosa")
        
        except ValueError:
            print("\nE' STATO INSERITO UN VALORE INCOMPATIBILE\n")
            pass

    for chiave in dizionario:
        voti = dizionario[chiave] 
        media = int((sum(dizionario[chiave])/(len(voti))))
        print("inserire se lo studente", chiave ,"ha preso la lode (si o no)")
        lode = input()
        if lode.capitalize() == "Si" and media < 30 or "Sì" and media < 30:
            media += 1
        dizionario_medie[chiave] = media

    for chiave in dizionario_medie:
        media = dizionario_medie[chiave]
        if media >= 27 and media <= 30:
            lista_nomi_a.append(chiave)
        elif media >= 24 and media <= 26:
            lista_nomi_b.append(chiave)
        elif media >= 18 and media <= 23:
            lista_nomi_c.append(chiave)
        else:
            print("la media non appartiene a nessuno degli intervalli dati")
    
    elenco_medie[(18,23)] = lista_nomi_c
    elenco_medie[(24,26)] = lista_nomi_b
    elenco_medie[(27,30)] = lista_nomi_a
    print(elenco_medie)

main()

#copyright Yanchen-Wang