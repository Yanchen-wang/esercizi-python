'''
Crea una classe Atleta per rappresentare le informazioni su un giocatore. 
La classe devve contenere un attributo booleano chiamato visitaMedica
Deve contenere un metodo per assegnare all'altleta il nome della suqadra dove gioca
Aggiungi alla classe Atleta un metodo chiamato effettua_visita che ponga l'attributo visita_medica uguale a True
Aggiungi alla classe un metodo per visuallizare i dati del giocatore
'''
class Atleta:
    def __init__(self, nome, cognome, anni, squadra = "Placeholder", visitaMedica = False):
        self.nome = nome
        self.cognome = cognome
        self.anni = anni
        self.squadra = squadra
        self.visitaMedica = visitaMedica

    def informazioni(self):
        if self.visitaMedica == False:
            visita_medica = "Positiva"
        else:
            visita_medica = "Negativa"
        print("Nome:",self.nome,"\nCognome:",self.cognome,"\nEta':",self.anni,"\nSquadra:",self.squadra,"\nNecessita' di una visita medica:",visita_medica)

    def aggiungere_squadra(self, nome_squadra):
        self.squadra = nome_squadra

    def effettua_visita(self):
        self.visitaMedica = True

while True:
    try:
        nome = input("inserire il nome dell'atleta\n").capitalize()
        cognome = input("inserire il cognome dell'atleta\n").capitalize()
        eta = int(input("inserire l'eta' dell'atleta\n"))
        squadra = input("inserire la squadra dell'atleta\n").capitalize()
        visita_medica = input("inserire se l'atleta ha eseguito la visita(si, no)\n").capitalize()
        informazioni = input("inserire 0 per visualizzare i dati dell'atleta, inserire qualsiasi altra cosa per continuare")
        a1 = Atleta(nome, cognome, eta)
        a1.aggiungere_squadra(squadra)
        
        if visita_medica == "Si":
            a1.effettua_visita()
        if informazioni == "0":
            a1.informazioni()
        
        trigger = input("inserire 0 per riavviare il programma, inserire qualsisasi altra cosa per interromperlo")
        if trigger != "0":
            break

    except ValueError:
        print("\nUNEXPECTED VALUE HAS BEEN INSERTED PLS ENTER A VALUE THAT CAN BE CONVERTED INTO AN INTEGER\n")
        continue