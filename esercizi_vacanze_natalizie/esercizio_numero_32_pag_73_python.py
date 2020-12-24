'''
Implementa l'algoritmo per il calcolo dellq soluzione di un'equazione di primo grado ax + b = 0. Il processo risolutivo 
dipende dai valori assunti dai coefficenti a e b secondo la tabella che segue:
         ________________a_______________
        |      = 0       |      !=0      |
________|________________|_______________|
| =  0  |  indeterminata |  impossibile  |
b_______|________________|_______________|
| != 0  |     x = 0      |   x = -(b/a)  |
|_______|________________|_______________|
'''
while True:
    try:
        print("per l'equazione ax + b = 0 :")
        a = int(input("inserire il valore del numero a"))
        b = int(input("inserire il valore del numero b"))
        if a == 0:
            if b == 0:
                print("l'equazione e' indeterminata")
            else:
                print("la soluzione dell'equazione e' x = 0")
        else:
            if b == 0:
                print("l'equazione e' impossibile")
            else:
                print("la soluzione dell'equazione e' x =",-(b/a))
        break
    except ValueError:
        print("\nE' STATO INSERITO UN VALORE INCOMPATIBILE\n")
        pass