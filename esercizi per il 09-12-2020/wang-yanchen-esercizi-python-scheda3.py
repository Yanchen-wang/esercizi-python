parola_norm = input("inserire la parola da tradurre in Rövarspråket\n")
vocali = "aeiouàèìòùAEIOU1234567890 "
while parola_norm != "0":
    parola_rövarspråket = ""
    for i in parola_norm:
        parola_rövarspråket = parola_rövarspråket + i
        if i not in vocali:
            parola_rövarspråket = parola_rövarspråket + "o" + i
    print("la parola tradotta in rövarspråket è",parola_rövarspråket)
    parola_norm = input("inserisca un'altra parola per continuare a tradurre , inserire 0 per fermarsi\n")