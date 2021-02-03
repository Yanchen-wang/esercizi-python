'''
Risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave e la capitale
come valore. Successivamente interroga il dizionario per visualizzare la capitale di una nazione.
'''
def crea_dizionario(lista_stati,lista_capitali):
    dizionario_stato_capitale = {}
    for stato in lista_stati:
        dizionario_stato_capitale[stato] = lista_capitali[lista_stati.index(stato)]
    return dizionario_stato_capitale

def main():
    lista_stati = ["Russia","Stati uniti","Canada","Italia","Francia","Regno unito","Spagna","Turchia","Iran","Cina","Giappone","Australia","Brasile","India","Messico","Indonesia","Polonia","Germania"]
    lista_capitali = ["Mosca","Washington DC","Ottawa","Roma","Parigi","Londra","Madrid","Ankara","Teheran","Pechino","Tokyo","Canberra","Brasilia","Nuova Delhi","Citta' del Messico","Giacarta","Varsavia","Berlino"]
    dizionario_stati_capitali = crea_dizionario(lista_stati,lista_capitali)
    while True:  
        nome_stato = input("inserire il nome dello stato cui vuoi visualizzare il nome della capitale, inserire nulla per fermare la sessione\n").capitalize()
        if nome_stato in dizionario_stati_capitali:
            print("la capitale dello stato inserito e'",dizionario_stati_capitali[nome_stato])
        elif nome_stato == "":
            print("PROGRAMMA INTERROTTO")
            break
        else:
            print("Mi dispiace non abbiamo a disposizione il nome della capitale dello stato inserito")
main()