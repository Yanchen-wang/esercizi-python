'''
Alla fine della giornata di elezioni per il ballottaggio tra due candidati, si
acquisiscono i voti ottenuti dai due candidati. Scrivi il programma che calcoli
le percentuali ottenute da ciascun candidato e comunichi il nome del vincitore.
'''
while True:
    try:
        voti1 = int(input("quanti voti ha ottemuto il candato x?"))
        voti2 = int(input("quanti voti ha ottemuto il candato y?"))
        print("il candidato x ha ottenuto il ",voti1/(voti1+voti2)*100,"% dei voti")
        print("il candidato y ha ottenuto il ",voti2/(voti1+voti2)*100,"% dei voti")
        break
    except ValueError:
        print("\nUNEXPECTED VALUE HAS BEEN INSERTED PLS ENTER A VALUE THAT CAN BE CONVERTED INTO AN INTEGER\n")
        pass
if voti1 > voti2:
    print("vince il candidato x")
elif voti1 == voti2:
    print("pareggio, si riconduce l'elezione")
else:
    print("vince il candidato y")