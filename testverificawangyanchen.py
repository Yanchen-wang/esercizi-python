from spalla import Verifica

Verifica.stampa_esercizi()
Verifica.firma("Yanchen Wang")

es = Verifica.inizia_esercizio(1)
es.consegna(es.dati.lower())

es = Verifica.inizia_esercizio(2)
es.consegna(es.dati * es.dati)

es = Verifica.inizia_esercizio(3)
es.consegna(es.dati["cognome"])

es = Verifica.inizia_esercizio(4)
es.consegna(len(es.dati))

es = Verifica.inizia_esercizio(5)
risultato = []
for parola in es.dati:
  risultato.append(parola.upper())
es.consegna(risultato)

es = Verifica.inizia_esercizio(6)
risultato = 0
for numero in es.dati:
  risultato += numero
es.consegna(risultato)

es = Verifica.inizia_esercizio(7)
risultato = 0
for numero in es.dati:
  if numero > 5:
    risultato += numero
es.consegna(risultato)

es = Verifica.inizia_esercizio(8)
risultato = 0
for i in range(len(es.dati)):
  numero = es.dati[i]
  if i % 2 == 0:
    risultato += numero
es.consegna(risultato)

es = Verifica.inizia_esercizio(9)
risultato = 0
for numero in es.dati:
  if numero % 2 == 1:
    risultato += numero
es.consegna(risultato)


es = Verifica.inizia_esercizio(10)
es.dati.sort()
es.consegna(es.dati)


es = Verifica.inizia_esercizio(11)
risultato = []
for parola in es.dati:
  risultato.append(parola.lower())
risultato.sort()
es.consegna(risultato)

es = Verifica.inizia_esercizio(12)
risultato = []
for numero in es.dati:
  risultato.append(numero - 1)
es.consegna(risultato)

es = Verifica.inizia_esercizio(13)
risultato = []
for i in range(len(es.dati)-1):
  numero = es.dati[i]
  successivo = es.dati[i+1]
  risultato.append(numero + successivo)
risultato.append(es.dati[-1])
es.consegna(risultato)

es = Verifica.inizia_esercizio(14)
risultato = {
  "positivi": 0,
  "negativi": 0,
  "zeri": 0
}
p = 0
n = 0
z = 0
for numero in es.dati:
  if numero < 0:
    risultato["negativi"] += 1
  elif numero > 0:
    risultato["positivi"] += 1
  else:
    risultato["zeri"] += 1
es.consegna(risultato)

es = Verifica.inizia_esercizio(15)
risultato = []
for parola in es.dati:
  if len(parola) % 2 == 0:
    risultato.append(parola.upper())
  else:
    risultato.append(parola.lower())
es.consegna(risultato)

es = Verifica.inizia_esercizio(16)
ultimo = es.dati.pop()
risultato = ""
for parola in es.dati:
  risultato += parola + " "
risultato += ultimo


es = Verifica.inizia_esercizio(17)
risultato = ""
for parola in es.dati:
  risultato += parola[-1]
es.consegna(risultato)

es = Verifica.inizia_esercizio(18)
risultato = ""
for parola in es.dati:
  if len(parola) > 4:
    risultato += parola[0]
es.consegna(risultato)

es = Verifica.inizia_esercizio(19)
risultato = []
for n in range(1, es.dati+1):
  if es.dati % n == 0:
    risultato.append(n)
es.consegna(risultato)

es = Verifica.inizia_esercizio(20)
risultato = []
for persona in es.dati:
  risultato.append(len(persona["figli"]))
es.consegna(risultato)

es = Verifica.inizia_esercizio(21)
risultato = []
for numero in es.dati:
  if numero <= 5:
    risultato.append(numero)
es.consegna(risultato)

es = Verifica.inizia_esercizio(22)
risultato = []
for numero in es.dati:
  if numero <= 6 and numero >= 3:
    risultato.append(numero)
es.consegna(risultato)

es = Verifica.inizia_esercizio(23)
risultato = 0
for persona in es.dati:
  risultato += persona["anni"]
es.consegna(risultato)

es = Verifica.inizia_esercizio(24)
risultato = []
for persona in es.dati:
  if persona["cognome"][0] == "C":
    risultato.append(persona["nome"])
es.consegna(risultato)

es = Verifica.inizia_esercizio(25)
risultato = 0
for frase in es.dati:
  for lettera in frase:
    if lettera == "a":
      risultato += 1
es.consegna(risultato)

es = Verifica.inizia_esercizio(26)
risultato = []
for numero in es.dati:
  risultato.append(numero * -1)
es.consegna(risultato)

es = Verifica.inizia_esercizio(27)
print(es)
risultato = []
for stoccaggio in es.dati:
  risultato += es.dati[stoccaggio]
print(risultato)