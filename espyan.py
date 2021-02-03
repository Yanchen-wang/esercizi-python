medie = []
dizionario = {
    "Alighieri" : [24,30,26],
    "Boccacio" : [18,22,24],
    "Manzoni" : [30,29,30]
}
elenco_medie = {
    (18,23) : "",
    (24,26) : "",
    (27,30) : ""
}
for key in dizionario:
    media = int((sum(dizionario.get(key))/3))
    print("inserire se lo studente", key ,"ha preso la lode (si o no)")
    lode = input()
    if lode == "si":
        media += 1
    medie.append(media)
def ottenere_chiave(valore):
    
for key in elenco_medie:
    for media in medie:
        if media in range(key)