'''
Oragnizza un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici. Fornito poi il nome della 
persona, il programma visulaizza il suo numero di telefono opurre un messaggio nel caso la persona non sia presente 
nella rubrica.
'''
nomi_numeri={
    "Marco":"3390938230",
    "Filippone":"0522694056",
    "Mario":"3480986421"
}

while True:
    nome = input("Inserire il nome della persona cui si vuole cercare (per interrompere il programma inserire a)")
    nome = nome.capitalize()
    if nome == "A":
        break
    elif nome in nomi_numeri:
        print("Il numero di", nome ,"è", nomi_numeri[nome])
    else:
        print("Contatto inesistente")
        aggiunta=input("Vuole aggiungere il contatto?(si, no)")
        if aggiunta=="si":
            print("Inserire il numero di", nome)
            numero=input()
            nomi_numeri[nome]=numero
            print("Numero aggiunto correttamente")