'''
Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista(nazione e relativa 
capitale si trovano nella medesima posizione delle rispettive liste), visualizza la capitale di una nazione della quale 
viene fornito da tastiera il nome, segnalando con un messaggio di errore il caso in cui la nazione rihiesta non sia 
compresa nell'elenco.
'''
def main():
    lista_stati = ["russia","stati uniti","canada","italia","francia","regno unito","spagna","turchia","iran","cina","giappone","australia","brasile","india","messico","indonesia","polonia","germania"]
    lista_capitali = ["Mosca","Washington DC","Ottawa","Roma","Parigi","Londra","Madrid","Ankara","Teheran","Pechino","Tokyo","Canberra","Brasilia","Nuova Delhi","Citta' del Messico","Giacarta","Varsavia","Berlino"]
    while True:
        nome_stato = input("inserire il nome dello stato cui vuoi visualizzare il nome della capitale, inserire nulla per fermare la sessione\n").lower()
        if nome_stato in lista_stati:
            print("la capitale dello stato inserito e'",lista_capitali[lista_stati.index(nome_stato)])
        elif nome_stato == "":   
            print("PROGRAMMA INTERROTTO")
            break
        else:
            print("Mi dispiace non abbiamo a disposizione il nome della capitale dello stato inserito")
main()