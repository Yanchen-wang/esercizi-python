'''
Costruisci un dizionario ottenuto da quello dell'esercizio precedente (16) invertendo il ruolo di chiave e valore.
Usa il nuovo dizionario per trovare il nome della nazione, noto il nome della capitale.
'''
dizionario_stati_capitali = {
    "Russia" : "Mosca",
    "Stati uniti" : 'Washington dc',
    "Canada" : "Ottawa",
    "Italia" : "Roma",
    "Francia" : "Parigi",
    "Regno unito" : "Londra",
    "Spagna" : "Madrid",
    "Turchia" : "Ankara",
    "Iran" : "Teheran",
    "Cina" : "Pechino",
    "Giappone" : "Tokyo",
    "Australia" : "Canberra",
    "Brasile" : "Brasilia",
    "India" : "Nuova delhi",
    "Messico" : "Citta del messico",
    "Indonesia" : "Giacarta",
    "Polonia" : "Varsavia",
    "Germania" : "Berlino"
}

def inverti_dizionario(dizionario):
    dizionario_invertito = {}
    for stato in dizionario:
        dizionario_invertito[dizionario[stato]] = stato
    return dizionario_invertito

def main():
    dizionario_capitali_stati = inverti_dizionario(dizionario_stati_capitali)
    while True:  
        nome_capitale = input("inserire il nome della capitale cui vuoi visualizzare il nome dello stato di appartenenza, inserire nulla per fermare la sessione\n").capitalize()
        if nome_capitale in dizionario_capitali_stati:
            print("lo stato a cui appartiene la capitale inserita e'", dizionario_capitali_stati[nome_capitale])
        elif nome_capitale == "":
            print("PROGRAMMA INTERROTTO")
            break
        else:
            print("Mi dispiace non abbiamo a disposizione il nome dello stato della capitale inserita")
main()