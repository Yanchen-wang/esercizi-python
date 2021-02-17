#Scrivi un programma che legga un reddito da tastiera e calcoli l'importo dell'imposta sul reddito e sull'imposta media
aliquote = {}
limiti = [15000, 28000, 55000, 75000, 1000000000000]
aliquota = [23, 27, 38, 41, 43]
imposta = 0
y = 0

for n in limiti:
    posizione = limiti.index(n)
    aliquote[n] = aliquota[posizione]

while True:
    try:
        reddito = float(input("inserire il reddito.\n"))
        z = reddito

        if z < 0 or z > 100000000000 :
            z = int("paolo")
        
        for i in aliquote:
            x = i - y
            print(x)

            if z <= i:
                imposta = imposta + (z / 100 * aliquote[i])
                break

            else:
                imposta = imposta + (x / 100 * aliquote[i])
                z = z - x
            y = i
        break
    
    except ValueError:
        print("\nUNEXPECTED VALUE HAS BEEN INSERTED PLS ENTER A VALUE THAT CAN BE CONVERTED INTO AN INTEGER\n")
        continue

print("Le tasse imposte sono", imposta ,"euro con tassazione media", round(imposta / reddito * 100, 2) ,"%")