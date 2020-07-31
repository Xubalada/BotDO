import re
class Personagem:
    def __init__(self, tela, debug = False):
        self.debug = debug
        self.tela = tela
        self.skils = None
        self.peso = None
        self.profissoes = []
        self.zaaps = []
       # self.viagem = Viagem(debug = self.debug, tela = self.tela) 
        self.character_status = self.get_my_status()

        

    def get_my_status(self):
        click(Region(180,756,11,4))#chat_box
        paste(ucode("%x%estatísticas%"))
        type(Key.ENTER)
        type(Key.ESC)
        wait(1)
        string_local = Region.text(Region(12,688,470,61))
        string_local_numbers = [int(number) for number in re.findall(r'(\d+)', string_local)]
        status_values = [sum(string_local_numbers[i:i+2]) for i in range(0, len(string_local_numbers), 2)]#https://stackoverflow.com/questions/42600533/optimize-sum-by-every-2-elements-in-list
        my_status = {"vitalidade": status_values[0],
                "sabedoria": status_values[1],
                "forca": status_values[2],
                "inteligencia": status_values[3],
                "sorte": status_values[4],
                "agilidade": status_values[5],
                "iniciativa": status_values[6],
                "pa": status_values[7],
                "pm": status_values[8]
                }
        return my_status


















personagem  = Personagem(Region(203,0,958,768))







############################################################################

all_zaaps = {
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
