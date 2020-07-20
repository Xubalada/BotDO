class Personagem:
    def __init__(self, tela, debug = False):
        self.debug = debug
        self.tela = tela
        self.skils = None
        self.peso = None
        self.profissoes = []
        self.zaaps = []
        self.viagem = Viagem(debug = self.debug, tela = self.tela) 

























############################################################################
class Personagem:
    def __init__(self):
        self.sikils = None
        self.peso = None
        self.profissoes = None
        self.zaaps = []
        from sikuli.Sikuli import *
        self.all_zaaps = {
                "Canto dos Papatudos" : [5,7],
                "Castelo de Amakna": [3,-5],
                "Limites da Floresta Malefica" : [-1,13],
                "Montanha dos Smagadores": [-5,-8],
                "Planicie dos Scarafolhas": [-1,24],
                "Porto de Madrestam": [7,-4],
                "Vilarejo de Amakna": [-2,0],
                "Cidade de Astrub": [5,-18],
                "Tainela": [1,-32],
                "Litoral sufokiano": [10,22],
                "(Sufokia)": [13,26],
                "Bonta": [-32,-56],
                "Brakmar": [-26,35],
                "Dunas das Ossadas": [15,-58],
                "Caminho das Caravanas": [-25,12],
                "Terras Profanadas": [-15,25],
                "Burgo": [-78,-41],
                "Vilarejo Soterrado": [-77,-73],
                "Praia da Tartaruga": [35,12],
                "Vilarejo Costeiro": [-46,18],
                "Vilarejo dos Zoths": [-53,18],
                "Vilarejo do Dossel": [-54,16],
                "Ilha da Cenouwa":[25,-4],
                "Vilarejo dos criadores": [-16,1],
                "Vilarejo de Ardala": [17,-31],
                "Vilarejo de Akwadala": [23,-22],
                "Vilarejo de Fogodala": [29,-49],
                "Suburbio de Pandala": [26,-37],
                "Vilarejo de Terradala": [30,-38],
                "Campos de Cania": [-27,-36],
                "Estradas Rochosas": [-20,-20],
                "Lago de Cania": [-3,-42],
                "Macico de Cania": [-13,-28],
                "Planicie dos Porkassos": [-5,-23],
                "Planicies Rochosas": [-17,-47],
                "Vilarejo dos Dopels": [-34,-8],
                "Crocuzko": [-83,-15],
                "Templo das Aliancas": [13,35],
                "Entrada do castelo de Traspafrent": [-67,-75],
                "Laboratorios abandonados": [27,-14],
                "Caminho das Almas": [-1,-3],
                "Cemiterio": [3,0],
                "Pastagens": [2,-5],
                "Vilarejo dos Diabretes": [-16,-24],
                "Vilarejo dos Kanigs": [0,-56],
                "Arco": [15,-20]
                }
    
    def get_zaaps(self):                
        
        for key in self.all_zaaps.keys():
            click(Pattern("1593921113688.png").targetOffset(70,1))
            type(key)
            if exists("1593924952372.png",0.2):
                self.zaaps.append(self.all_zaaps[key])
                
                print(self.zaaps)
            click("1593923807674.png")
            
