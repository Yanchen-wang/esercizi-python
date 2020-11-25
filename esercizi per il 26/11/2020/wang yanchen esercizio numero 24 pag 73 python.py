voti1 = int(input("quanti voti ha ottemuto il candato x?"))
voti2 = int(input("quanti voti ha ottemuto il candato y?"))
print("il candidato x ha ottenuto il ",voti1/(voti1+voti2)*100,"% dei voti")
print("il candidato y ha ottenuto il ",voti2/(voti1+voti2)*100,"% dei voti")
if voti1 > voti2:
    print("vince il candidato x")
elif voti1 == voti2:
    print("pareggio, si riconduce l'elezione")
else:
    print("vince il candidato y")