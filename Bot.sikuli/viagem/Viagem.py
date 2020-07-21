from sikuli.Sikuli import *
from java.awt import Robot
import re
ALL_ZAAPS =  {
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
    "Arco de Vili": [15,-20]
}
    




class Viagem:
    
    def __init__(self, tela, debug = False):
        self.debug = debug
        self.tela = tela
        self.checkerror = CheckError()
        #comeca tela
        self.border_left = self.tela.left_border
        self.border_top = self.tela.top_border
        self.border_right = self.tela.right_border
        self.border_down = self.tela.botton_border
        self.chat_write_box_position = self.tela.chat_write_box_position
        self.chat_window_position =  self.tela.chat_window_position
        #termina tela
        self.destination = None
        self.currentLocation = self.get_current_location()
        self.character_zaaps = []
        self.get_character_zaaps()
        
        
        
    
    def go_to(self, name = None, position = None):
        if position is not None:
            self.set_destiny(position)
            where_to_start_moving = self.find_start_position()
            if(where_to_start_moving !=self.currentLocation):
                self.go_to_zaap(where_to_start_moving)
                self.currentLocation = where_to_start_moving
            self.walk_to(self.destination)
            
                
            
    
    def go_to_zaap(self, zaap_to_go):
        self.open_sacola()
        self.open_zaap()
        zaap_name = self.get_zaap_name_by_position(zaap_to_go)
        self.select_zaap_by_name(zaap_name)
        type(Key.ENTER)
        sleep(3)
        

    def select_zaap_by_name(self, name):
        click("images/viagem/1593923807674.png")
        click(Pattern("images/viagem/1593921113688.png").targetOffset(70,1))
        type(name)
        if exists("images/viagem/1593924952372.png",0.2):
            return True
        return False



        
    def get_zaap_name_by_position(self, positon): 
        for zaap_name, zaap_position in ALL_ZAAPS.items(): 
            if positon == zaap_position: 
                return zaap_name 
    
        return "zaap_name doesn't exist"
        
    def set_destiny(self, pos):
        self.destination = pos      
    
    def get_current_location(self, count = 0):       
        if count > 3:
            return None
        click(self.chat_write_box_position)
        type("%pos%")
        sleep(1)
        type(Key.ENTER)
        sleep(1)
        #Checa o erro de mensagem repetida
        self.checkerror.check_chat()
        stringLocal = Region.text(self.chat_window_position)
        chat_positions = re.findall(r'(\[-?\d+,-?\d+\])', stringLocal)
        self.checkerror.clean_chat()
        #type(Key.ESC)
        if len(chat_positions)> 0:
            return eval(chat_positions[-1])
        else:
            count = count + 1
            self.get_current_location(count)
                  
        
    def get_dist(self, coord1, coord2):
        calc_dist = abs(coord1[0]-coord2[0])+ abs(coord1[1]-coord2[1])
        return calc_dist   

    def find_start_position(self):
        zaap_list = self.character_zaaps
        zaap_list.append(self.currentLocation)
        zaap_dist = []
        for i in zaap_list:
            zaap_dist.append(self.get_dist(self.destination,i))

        return zaap_list[zaap_dist.index(min(zaap_dist))]

    def get_character_zaaps(self):
        if self.debug:
            self.character_zaaps = [
                [5,7], [3,-5], [-1,13], [-5,-8],
                [-1,24], [7,-4], [-2,0], [5,-18],
                [1,-32], [10,22], [13,26], [-32,-56],
                [-26,35], [15,-58], [-25,12], [-15,25],
                [-78,-41], [-77,-73], [35,12], [-46,18],
                [-53,18], [-54,16], [25,-4], [-16,1], [17,-31],
                [23,-22], [29,-49], [26,-37], [30,-38],
                [-27,-36], [-20,-20], [-3,-42], [-13,-28], 
                [-5,-23], [-17,-47], [-34,-8], [-83,-15], [13,35], 
                [-67,-75], [27,-14], [-1,-3], [3,0], [2,-5],
                [-16,-24], [0,-56], [15,-20]
            ]      
            return
        self.open_sacola()
        for key in ALL_ZAAPS.keys():
            click(Pattern("images/viagem/1593921113688.png").targetOffset(70,1))
            type(key)
            if exists("images/viagem/1593924952372.png",0.2):
                self.character_zaaps.append(ALL_ZAAPS[key])
                
            click("images/viagem/1593923807674.png")
        self.close_sacola()

    def close_zaap(self):
        if exists(Pattern("images/viagem/1593904497356.png").similar(0.57)):
            type(Key.ESC)
        sleep(2)

    def close_sacola(self):
        self.close_zaap()
        if exists("images/viagem/1593899805636.png"):
            type("h")
        sleep(2)
        
            

    def open_sacola(self):
        if not exists("images/viagem/1593899805636.png"):
            type("h")
        CheckError().sacola_viagem()            
        sleep(2)
        self.open_zaap()
        
    def open_zaap(self):
        if not exists(Pattern("images/viagem/1593904497356.png").similar(0.54)):
           
            click( Pattern("images/viagem/1593890332318.png").similar(0.75))
        sleep(2)

            

    def walk_right(self,xtimes):
        contador_righ = 0
        while contador_righ < xtimes:
            click(self.border_right)
            contador_righ += 1
            print(contador_righ)
            print(self.border_right)
            sleep(7)
            
    def walk_left(self,xtimes):
        contador_left = 0
        while contador_left < xtimes:
            click(self.border_left)
            contador_left += 1
            print(contador_left)
            print(self.border_left)
            sleep(7)

    def walk_top(self,xtimes):
        contador_top = 0
        while contador_top < xtimes:
            click(self.border_top)
            contador_top += 1
            print(contador_top)
            print(self.border_top)
            sleep(7)
            
    def walk_down(self,xtimes):
        contador_down = 0
        while contador_down < xtimes:
            click(self.border_down)
            contador_down += 1
            print(contador_down)
            print(self.border_down)
            sleep(7)
    
    def walk_to(self, destiny):
        if destiny == self.currentLocation:

            pass
        vetor_deslocamento = [self.currentLocation[0] - destiny[0],
                              self.currentLocation[1] - destiny[1]]
        if vetor_deslocamento[0] <= 0:
            self.walk_right(abs(vetor_deslocamento[0]))
        else:
            self.walk_left(abs(vetor_deslocamento[0]))
        if vetor_deslocamento[1] <= 0:
            self.walk_down(abs(vetor_deslocamento[1]))
        else:
            self.walk_top(abs(vetor_deslocamento[1]))
        sleep(3)