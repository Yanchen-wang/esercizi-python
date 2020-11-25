x = 0
y = 0 
z = 0
while x != -1:
    print("inserire lo stipendio di ciascun dipendente in euro,inserire -1 per terminare il processo ")
    x = int(input())
    y += x 
    z += 1
print("la media degli stipendi e' di",y/z,"euro")