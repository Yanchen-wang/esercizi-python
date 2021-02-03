def area( base_M, base_m, altezza):
    area = (base_M + base_m)*altezza/2
    return area

def perimetro( base_M, base_m, altezza, tipo_trapezio):
    p1 = base_M-base_m
    if tipo_trapezio == "isoscele":
        lato_obliquo1 = (((p1/2)**2)+(altezza**2))**(1/2)
        lato_obliquo2 = lato_obliquo1
    elif tipo_trapezio == "rettangolo":
        lato_obliquo1 = (((p1)**2)+(altezza**2))**(1/2)
        lato_obliquo2 = altezza
    else:
        lato_obliquo1 = int(input("inserire la lunghezza del primo lato obliquo del triangolo scaleno"))
        lato_obliquo2 = int(input("inserire la lunghezza del secondo lato obliquo del triangolo scaleno"))
    perimetro = base_M + base_m + lato_obliquo1 + lato_obliquo2
    return perimetro

while True:
    try:
        trapezio = input("a che tipo appartiene il trapezio?(isoscele, rettangolo, scaleno)")
        base_maggiore = int(input("inserire la lunghezza della base maggiore del trapezio"))
        base_minore = int(input("inserire la lunghezza della base minore del trapezio"))
        altezza = int(input("inserire la lunghezza dell'altezza del trapezio"))
        area = area( base_maggiore, base_minore, altezza)
        print("l'area del trapezio e' ", area)
        perimetro = perimetro( base_maggiore, base_minore, altezza, trapezio)
        print("il perimetro del trapezio e'", perimetro)
        break
    except ValueError:
        print("INSERITO VALORE INCOMPATIBILE")
        pass