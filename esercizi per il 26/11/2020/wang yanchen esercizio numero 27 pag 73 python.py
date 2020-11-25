x = 0
y = 0 
while x != 0:
    print("inserire il numero dei veicoli transitati in ciascun giorno del periodo considerato per l'entrata del casello dell'autostrada,inserire 0 per indicare il termine del periodo considerato")
    x = int(input())
    y += x 
print("in tutto",y,"veicoli sono transitati durante periodo considerato")