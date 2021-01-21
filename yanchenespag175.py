def ok():
    dic_ita_ing = {}
    for i in range(7):
        print("giorno" + str(i+1) + ":")
        giorno = input().split(",")
        dic_ita_ing[giorno] = ""