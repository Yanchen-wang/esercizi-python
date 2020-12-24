'''
In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto "rövarspråket", che significa 
"linguaggio dei furfanti": consiste nel raddoppiare ogni consonante dì una parola e inserire una "o" nel mezzo.
Ad esempio la parola "mangiare" diventa "momanongogiarore". Scrivi una programma in grado di tradurre una parola o frase
passata tramite input in "rövarspråket".
Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta 
positiva, dovrà attendere l'inserimento di una nuova parola da parte dell'utente. 
'''
parola_norm = input("inserire la parola da tradurre in Rövarspråket\n")
vocali = "aeiouàèìòùAEIOU1234567890 "
while parola_norm != "0":
    parola_rovarspraket = ""
    for i in parola_norm:
        parola_rovarspraket = parola_rovarspraket + i
        if i not in vocali:
            parola_rovarspraket = parola_rovarspraket + "o" + i
    print("la parola tradotta in rövarspråket è",parola_rovarspraket)
    parola_norm = input("inserisca un'altra parola per continuare a tradurre , inserire 0 per fermarsi\n")