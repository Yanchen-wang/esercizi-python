def ita_ing():
    dic_ita_ing = {} 
    for i in range(7):
        print("giorno numero" + str(i+1) + ":")
        giorno = input()
        print("day number" + str(i+1) + ":")
        day = input()
        dic_ita_ing[giorno] = day
    return dic_ita_ing 

def main():
    print("inserire i nomi di ciascun giorno della settimana in italiano e inglese")
    settimana = ita_ing()
    print("dizionario ita-ing:",settimana)

main()