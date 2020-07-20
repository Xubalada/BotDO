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
        click("1593923807674.png")
        click(Pattern("1593921113688.png").targetOffset(70,1))
        type(name)
        if exists("1593924952372.png",0.2):
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
            click(Pattern("1593921113688.png").targetOffset(70,1))
            type(key)
            if exists("1593924952372.png",0.2):
                self.character_zaaps.append(ALL_ZAAPS[key])
                
            click("1593923807674.png")
        self.close_sacola()

    def close_zaap(self):
        if exists(Pattern("1593904497356.png").similar(0.57)):
            type(Key.ESC)
        sleep(2)

    def close_sacola(self):
        self.close_zaap()
        if exists("1593899805636.png"):
            type("h")
        sleep(2)
        
            

    def open_sacola(self):
        if not exists("1593899805636.png"):
            type("h")
        CheckError().sacola_viagem()            
        sleep(2)
        self.open_zaap()
        
    def open_zaap(self):
        if not exists(Pattern("1593904497356.png").similar(0.54)):
           
            click( Pattern("1593890332318.png").similar(0.75))
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
        
        
        

class Personagem:
    def __init__(self, tela, debug = False):
        self.debug = debug
        self.tela = tela
        self.skils = None
        self.peso = None
        self.profissoes = []
        self.zaaps = []
        self.viagem = Viagem(debug = self.debug, tela = self.tela) 
        
    

            

class CheckError:

    def clean_chat(self):
        click(Pattern("1593972303685.png").targetOffset(-655,37))
        type("/clear")
        type(Key.ENTER)
        type(Key.ESC)

    def check_chat(self):
        if exists(Pattern("1593974580043.png").similar(0.59)):
            click(Pattern("1593972303685.png").targetOffset(-655,37))
            type("Ai!")
            type(Key.ENTER)
        
        
        

    def sacola_viagem(self):
        if Region(212,640,277,128).exists("1593886301433.png",2):
            #fix error
            self.clean_chat()


    def disconect(self):
        if Region(472,296,437,195).exists("1593887737569.png",1.5):
            #AJEITAR AINDA
            pass




class Tela:
    def __init__(self):
        self.action_screen = self.get_action_screen_position()
        self.left_border = None
        self.top_border = None
        self.right_border = None
        self.botton_border = None
        self.get_borders_position()
        self.top_border.highlight(1)
        self.chat_write_box_position = self.get_chat_write_box_position()
        self.chat_window_position = Region(self.chat_write_box_position.getX(),
                       self.chat_write_box_position.getY() - 97,
                       self.chat_write_box_position.getW(),
                       97)

    def get_screen_position(self):
        screen_reg = find(capture())    
        return Region(screen_reg.getX(),screen_reg.getY(),screen_reg.getW(),screen_reg.getH())
        
    def get_action_screen_position(self):
        popup("capture the screen where the action occuours")
        action_screen = self.get_screen_position()
        return action_screen
        
    def get_borders_position(self):
        axe_x = self.action_screen.getX()
        axe_y = self.action_screen.getY()
        width = self.action_screen.getW()
        high = self.action_screen.getH()
        self.left_border = Region(axe_x, axe_y, width/100, high)
        self.top_border = Region(axe_x, axe_y, width, high/100)
        self.right_border = Region(axe_x + (width - width/100), axe_y, width/100, high)
        self.botton_border = Region(axe_x,axe_y + (high - high/100),width, high/100)
        
    def get_chat_write_box_position(self):
        popup("Select the chat write box position")
        return self.get_screen_position()


    def start_battle(self):
        popup("deu")

    def battle_start_observe(self):
       r = self.action_screen
       r.onAppear("1594763193470.png", self.start_battle())
       r.observeInBackground()
       wait(30)

    def battle_detect(self):
        onAppear("1594766090257.png", self.start_battle) # or any other onXYZ()
        observeInBackground()

    def start_battle(self,event):
        if event.isAppear():
            self.battle = Battle()


       
class Battle:
    def __init__(self, tela):
        self.tela = tela
        self.action_screen = self.tela.action_screen
        self.chat_write_box_position = self.tela.chat_write_box_position
        self.chat_window_position =  self.tela.chat_window_position
        self.checkerror = CheckError()
        popup("pega luta")
        self.screen_first_sample =  Finder(Image.create(Pattern(capture(self.action_screen)).similar(0.9)))
        self.screen_first_sample.setFindChangesImageDiff(5)
        self.step_x = self.action_screen.getW()/14.5
        self.step_y = self.action_screen.getH()/41
        self.map = []
        self.map_cells = []
        self.map_holes = []
        self.map_walls = []
        self.pa = None
        self.pm = 5
        self.get_map_info()
        popup("comeca round")
        self.monsters_position = self.find_monsters()
        self.my_current_position = self.find_me()
        self.closest_monster = self.get_closest_monster()
        #self.get_start_battle_positions()
        self.Maertelo_da_Lua = [4,7,2,"ar",38,47]
        #self.go_to_closest_monster()
        self.use_skill(self.Maertelo_da_Lua) 
        wait(10)
        #self.spells_sample = Finder(Image.create(Pattern(capture(Region(942,740,117,25)))))
        #self.spells_sample.setFindChangesImageDiff(50)
################################## principal, informacao do mapa ############################        
    def get_row_position(self, row_number):
        return int(self.action_screen.getY()+ self.step_y*row_number)

    def get_column_position(self, column_number, row_number):
        white_row_translation = self.action_screen.getW()/29
        if row_number % 2 != 0:
            white_row_translation = 0
        return int(self.action_screen.getX()+self.step_x+ self.step_x*column_number - white_row_translation )


    def get_map_info(self):
        count_index = 0
        count_rows = 0
        while count_rows < 40:
            count_columns = 0
            while count_columns < 14:
                coord_x = self.get_column_position(count_columns,count_rows)
                coord_y = self.get_row_position(count_rows) + 10
                pixel_color = Robot().getPixelColor(coord_x, coord_y) # get the color object
                color = [pixel_color.getRed(), pixel_color.getGreen(), pixel_color.getBlue()]#array [R,G,B] 
                #print color[0],color[1],color[2]
                # 0 -> cells                
                # 1 -> holes
                # 2 -> walls
                if 100 < color[0]:
                    self.map.append(0)
                    self.map_cells.append(count_index)
                elif  color[0] <= 30:
                    self.map.append(1)
                    self.map_holes.append(count_index)
                elif 65 < color[0] <= 100:
                    self.map.append(2)
                    self.map_walls.append(count_index)
                elif 30 < color[0] <= 65:
                    self.map.append(0)#monsters
                    self.map_cells.append(count_index)
                count_index += 1
                count_columns += 1
            count_rows += 1        

    def map_pos_to_screen_point(self, index_in_map):# traduz a posicao da lista no self.mapa para um ponto da tela
        row_number = index_in_map//14
        column_number = abs(index_in_map-((index_in_map//14) * 14))
        row = self.get_row_position(row_number)
        column = self.get_column_position(column_number, row_number)
        reg = Region(column,row+10,0,0)
        return reg


########################################### encontrar algo no mapa ##############################
    def find_monsters(self): # returns array of map_index position
        self.monsters = []
        for cell in self.map_cells:
            point = self.map_pos_to_screen_point(cell)
            point_color = Robot().getPixelColor(point.getX(), point.getY())
            if 30 < point_color.getRed() < 65:
                self.monsters.append(cell)
                point.highlight()
        return self.monsters

    def find_characters(self):# returns array of map_index position
        self.characters = []
        for cell in self.map_cells:
            point = self.map_pos_to_screen_point(cell)
            point_color = Robot().getPixelColor(point.getX(), point.getY())
            if 100 < point_color.getRed() < 260:
                if point_color.getBlue() < 80:
                    self.characters.append(cell)
                    point.highlight()       
        return self.characters

    def find_me(self):#### versao sem Tela(), que oferece self.chat_write_box_position
        click(self.chat_write_box_position)
        type("/cellid")
        type(Key.ENTER)####################incluir checkerror_clean
        wait(1)
        string_chat = Region.text(self.chat_window_position)
        cell_id = re.findall(r'Célula atual: (\d+)', string_chat)
        self.checkerror.clean_chat()
        return eval(cell_id[-1])
##########################################################################################################################
    def check_top(self,central_position, some_map):
        if central_position < 14:
            return None
        if central_position /14/2 == 0:
            return None
        if (central_position//14)%2 ==0:
            if central_position -15 not in some_map:
                return None
            if central_position - 15 in self.monsters_position:
                return None
            return central_position -15
        if central_position -14 not in some_map:
            return None
        #if central_position - 14 in self.monsters_position:
           # return None
        return central_position - 14

    def check_botton(self,central_position, some_map):
        if central_position > 545:
            return None
        if (central_position + 1)% 28 == 0: 
            return None
        if (central_position//14)% 2 == 0:
            if central_position + 14 not in some_map:
                return None
            if central_position + 14 in self.monsters_position:
                return None
            return central_position + 14
        if central_position +15 not in some_map:
            return None
        #if central_position + 15 in self.monsters_position:
            #return None
        return central_position + 15           
                
    def check_left(self,central_position, some_map):
        if central_position > 545:
            return None
        if central_position /14/2 == 0:
            return None
        if (central_position//14)% 2 == 0:
            if central_position + 13 not in some_map:
                return None
            return central_position + 13
        if central_position +14 not in some_map:
            return None
        return central_position + 14           

    def check_right(self,central_position, some_map):
        if (central_position + 1)% 28 == 0: 
            return None
        if central_position < 14:
            return None
        if (central_position//14)% 2 == 0:
            if central_position - 14 not in some_map:
                return None
            if central_position - 14 in self.monsters_position:
                return None
            return central_position - 14
        if central_position - 13 not in some_map:
            return None
        #if central_position - 13 in self.monsters_position:
            #return None
        return central_position - 13 

    def get_neighborhood(self,central_position, some_map):
        neighborhoods = []
        right_neighborhood = self.check_right(central_position, some_map)
        left_neighborhood = self.check_left(central_position, some_map)
        top_neighborhood = self.check_top(central_position, some_map)
        botton_neighborhood = self.check_botton(central_position, some_map)
        if right_neighborhood != None:
            neighborhoods.append(right_neighborhood)
        if left_neighborhood != None:
            neighborhoods.append(left_neighborhood)
        if top_neighborhood != None:
            neighborhoods.append(top_neighborhood)
        if botton_neighborhood != None:
            neighborhoods.append(botton_neighborhood)
        return neighborhoods    

    def dijkstra_algorithim(self,central_position, destiny):
        point_distance = [[central_position]]
        uncovered_cells = list(self.map_cells)
        position = 0
        stop = False
        while stop == False:
            possible_cells = []
            for cell in point_distance[position]:
                neighborhood = self.get_neighborhood(cell, uncovered_cells)
                for pos in neighborhood:   
                    uncovered_cells.remove(pos)
                    possible_cells.append(pos)
                    if pos == destiny:
                        stop = True
                        break
                if stop == True:
                    break
            point_distance.append(possible_cells)
            position += 1
        return point_distance

    def get_best_way(self, dijkstra_list , destiny):
        possible_ways = dijkstra_list
        current_cell = destiny
        best_way = []
        while len(possible_ways) != 1:
            possible_ways.remove(possible_ways[-1])
            cell_neighborhoods = self.get_neighborhood(current_cell, self.map_cells)
            for cell in cell_neighborhoods:
                if cell in possible_ways[-1]:
                    best_way.append(cell)
                    current_cell = cell
                    break
        return best_way

    def get_closest_monster(self):
        point_distance = [[self.my_current_position]]
        uncovered_cells = list(self.map_cells)
        position = 0
        while set(self.monsters_position) & set(point_distance[position]) == set([]):
            possible_cells = []
            for cell in point_distance[position]:
                neighborhood = self.get_neighborhood(cell, uncovered_cells)
                for pos in neighborhood:
                    uncovered_cells.remove(pos)
                    possible_cells.append(pos)
            #for cell in possible_cells:
                #self.map_pos_to_screen_point(cell).highlight()
            point_distance.append(possible_cells)
            position += 1
        closest_monsters = list(set(self.monsters_position) & set(point_distance[position]))
        return [closest_monsters[0], point_distance]

    def go_to_closest_monster(self):
        closest_monster_info = self.closest_monster
        best_way = self.get_best_way(closest_monster_info[1], closest_monster_info[0])
        for way in best_way:
            self.map_pos_to_screen_point(way).highlight()
        click(self.map_pos_to_screen_point(best_way[-(self.pm + 1 )])) 

    def check_skill_range(self,skill):
        monster_info = self.closest_monster
        print monster_info
        a = len(monster_info[1])
        print a
        if skill[0] <= a <= skill[1]:
            return monster_info[0]
        return False

    def use_skill(self,skill):
        monster = self.check_skill_range(self.Maertelo_da_Lua)
        if monster == False:
            return None
        type(str(skill[2]))
        click_reg = self.map_pos_to_screen_point(monster)
        click(click_reg)
        click(self.map_pos_to_screen_point(monster))
        wait(10)
############################################## possivel Lixo ############################################################################

    def get_screen_changes(self, screen_region, time_interval):
        changes = []
        action_x = self.action_screen.getX()
        action_y = self.action_screen.getY()
        sleep(time_interval)
        action_screen_changes = self.screen_first_sample.findChanges(capture(screen_region))
        for region in action_screen_changes:
            region = Region(region.getX()+action_x,region.getY()+action_y,region.getW(),region.getH())
            changes.append(region)
        return changes

    def get_spell_region_changes(self,spell_region): 
        spell_changes = []
        translation_x = spell_region.getX()
        translation_y = spell_region.getY()
        region_changes = self.spells_sample.findChanges(capture(spell_region))
        for region in region_changes:
            region = Region(region.getX()+translation_x,region.getY()+translation_y,region.getW(),region.getH())
            spell_changes.append(region)
        return spell_changes

            
    def get_start_battle_positions(self):# incompleto
        start_position = []
        my_team = None
        for cell in self.map_cells:
            point = self.map_pos_to_screen_point(cell)
            point_color = Robot().getPixelColor(point.getX(), point.getY())
            color = [point_color.getRed(),point_color.getBlue()]
            if 220 < color[0]:
                start_position.append(cell)
                my_team = "red"
                continue
            if 220 < color[1]:
                start_position.append(cell)
                my_team = "blue"
        for a in start_position:
            self.map_pos_to_screen_point(a).highlight()
        wait(10)
        return [my_team,start_position]        
    

tela_toda = Region(216,23,932,661)




    
        
        
tela = Tela()
battle = Battle(tela)
#personagem = Personagem(debug = True, tela = tela)

#personagem.viagem.go_to(position = [-22,39])



#tela.get_borders_position()
#tela._position()