'''
Scrivi un programma che a scelta dall'utente calcoli l'area di un quadrato, rettangolo triangolo e cerchio.
'''
normal = True
while normal == True:
    poligono = input("scegli di quale dei seguenti poligoni vuoi calcolare l'area : quadrato,rettangolo,triangolo,cerchio\n")
    unità_misura = input("inserire l'unità di misura utilizzata\n")
    poligono = poligono.lower()
    normal = False
    try:
        if poligono == "quadrato":     
            l = int(input("inserisci la lunghezza del lato\n"))
            print("l'area del quadrato e' di",l**2,unità_misura,"quadrati")
        elif poligono == "rettangolo":
            b = int(input("inserisci la lunghezza della base\n"))
            h = int(input("inserisci la lunghezza dell'altezza\n"))
            print("l'area del rettangolo e' di,",b*h,unità_misura,"quadrati")
        elif poligono == "triangolo":
            b = int(input("inserisci la lunghezza della base\n"))
            h = int(input("inserisci la lunghezza dell'altezza\n"))
            print("l'area del triangolo e' di,",b*h/2,unità_misura,"quadrati")
        elif poligono == "cerchio":
            r = int(input("inserisci la lunghezza del raggio\n"))
            print("l'area del cerchio e' di",r**2*3.14,unità_misura,"quadrati")
        else:
            print(poligono,"non e' uno dei poligoni disponibili al calcolo dell'area, inserisca uno dei poligoni disponibili")
            normal = True
    except ValueError:
        print("\nE' STATO INSERIRITO UN VALORE CHE NON PUO ESSERE CONVERTITO IN INTEGER\n")
        normal = True
        pass