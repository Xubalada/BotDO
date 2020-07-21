import sys

mySikuliPath = "C:\\Sikulix\\BotDO\\Bot.sikuli\\"
if not mySikuliPath in sys.path: sys.path.append(mySikuliPath)
from tela import Tela
from viagem import Viagem
from character import Personagem

class Menu:
    def __init__(self,prof = False):
        self.prof = prof

    def escolher(self):
        self.prof = select("Escolha uma profissao", options = ("Alquimista","Fazendeiro","Lenhador","Mineiro","Pescador"))
        confirma = popAsk("Voce selecionou:"+self.prof+"?")
        if confirma == True:
            if self.prof == "Alquimista":
                popup("Alquimista")
            elif self.prof == "Fazendeiro":
                popup("Fazendeiro")
            elif self.prof == "Lenhador":
                popup("Lenhador")
            elif self.prof == "Mineiro":
                popup("Mineiro")
            elif self.prof == "Pescador":
                popup("Pescador")
        else:
            Menu().escolher()

tela = new Tela()
personagem = Personagem(debug = True, tela = tela)

personagem.viagem.go_to(position = [-22,39])
viagem.