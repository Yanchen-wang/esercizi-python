'''
Data la parabola y = ax^2 + bx + c, definisci tre funzioni per calcolarne la i punti significativi: vertice, fuoco,
intersezione con gli assi. Le tre funzioni ricevono come parametri i coefficenti a, b, c e restituscono il valore 
calcolato(Non fate l'intersezione con gli assi. I parametri a, b, c vanno inseriti dall'utente.)
'''

def vertice (a, b, c):
    x_vertice = -b/(2*a)
    y_vertice = -(b**2-4*a*c)/(4*a)
    return (x_vertice, y_vertice)


def fuoco (a, b, c):
    x_fuoco = -(b/(2*a))
    y_fuoco = (1-(b**2-4*a*c))/(4*a)
    return (x_fuoco, y_fuoco)

a = int(input("inserire il valore del coefficente a"))
b = int(input("inserire il valore del coefficente b"))
c = int(input("inserire il valore del coefficente c"))
coordinate_vertice = vertice(a, b, c)
coordinate_fuoco = fuoco(a, b, c)
print("le coordinate del vertice della parabola sono:",coordinate_vertice)
print("le coordinate del fuoco della parabola sono:",coordinate_fuoco)