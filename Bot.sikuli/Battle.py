from java.awt import Robot
import time
import re
class Battle:
    def __init__(self, action_screen):
        self.action_screen = action_screen
        self.screen_first_sample =  Finder(Image.create(Pattern(capture(self.action_screen)).similar(0.9)))
        self.screen_first_sample.setFindChangesImageDiff(5)
        self.step_x = self.action_screen.getW()/14.5
        self.step_y = self.action_screen.getH()/41
        self.map = []
        self.map_cells = []
        self.map_holes = []
        self.map_walls = []
        popup("stop")
        self.pa = None
        self.pm = 5
        self.get_map_info()
        self.get_start_battle_positions()
        self.monsters_position = self.find_monsters()
        self.my_current_position = self.find_me()
        self.go_to_start_position()
        popup("inicia")
        self.closest_monster = self.get_closest(self.my_current_position, self.monsters_position)
        #self.get_start_battle_positions()
        self.my_skills = [["martelo_da_lua",4,7,2,"agi",38,47],["Furia",1,1,3,"agi",39,43]] #[name, min_range, max_range, element, damage_min,damage_max]
        self.use_skill(self.Maertelo_da_Lua)
        self.go_to_closest_monster()
        wait(10)
        #self.spells_sample = Finder(Image.create(Pattern(capture(Region(942,740,117,25)))))
        #self.spells_sample.setFindChangesImageDiff(50)

    def get_hp(self):
        click(Region(173,759,9,5))#janela de escrita
        type("%hp%")
        type(Key.ENTER)####################incluir checkerror_clean
        wait(1)
        string_chat = Region.text(Region(12,683,475,67))#janela do char
        cell_id = re.findall(r': (\d+)', string_chat)
        return eval(cell_id[-1])

    def get_pa_pm(self):
        type("c")
        
    
    def do_round_task(self):#incompleto
        self.monsters_position = self.find_monsters()
        self.my_current_position = self.find_me()
        self.hp = self.get_hp()
        
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
                elif color[0] <= 30:
                    if color[2] > 50:
                        self.map.append(0)
                        self.map_cells.append(count_index)
                    else:
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
        click(Region(173,759,9,5))
        type("/cellid")
        type(Key.ENTER)####################incluir checkerror_clean
        wait(2)
        string_chat = Region.text(Region(0,684,487,65))
        cell_id = re.findall(r'Célula atual: (\d+)', string_chat)
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
            cell_neighborhoods = self.get_neighborhood(current_cell, x)
            for cell in cell_neighborhoods:
                if cell in possible_ways[-1]:
                    best_way.append(cell)
                    current_cell = cell
                    break
        return best_way
                                            #monsters
    def get_closest(self, center, list_group):
        point_distance = [[center]]
        uncovered_cells = list(self.map_cells)
        position = 0
        while set(list_group) & set(point_distance[position]) == set([]):
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
        closest_item_position = list(set(list_group) & set(point_distance[position]))
        return [closest_item_position[0], point_distance]

    def go_to_closest_monster(self):
        closest_monster_info = self.closest_monster
        best_way = self.get_best_way(closest_monster_info[1], closest_monster_info[0])
        if len(closest_monster_info[1]) != 2:          
            for way in best_way:
                self.map_pos_to_screen_point(way).highlight()
            click(self.map_pos_to_screen_point(best_way[-(self.pm + 1 )])) 

    def check_skill_range(self,skill):
        monster_info = self.closest_monster
        print monster_info
        range_skill = len(monster_info[1])
        print range_skill
        if skill[0] <= range_skill <= skill[1]:
            return monster_info[0]
        return False

    def check_my_skills(self):
        avaliable_skills = []
        for skill in self.my_skills:
            skill_range = self.check_skill_range(skill)
            if skill_range != False:
                avaliable_skills.append([skill,skill_range])
        return avaliable_skills
    
    def use_skill(self,skill,target):
        type(str(skill[2]))
        click(self.map_pos_to_screen_point(target))
        click(self.map_pos_to_screen_point(target)) 
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
        return start_position       
    
    def find_best_start_position(self):
        start_position = self.get_start_battle_positions()
        monsters = self.monsters_position
        start_list = []
        for position in start_position:
            best_start = self.get_closest(position, monsters)
            start_list.append(len(best_start[1]) - 1 )
        return start_position[start_list.index(min(start_list))]
            
    def go_to_start_position(self):
        start_position = self.find_best_start_position()
        click(self.map_pos_to_screen_point(start_position))


tela_toda = Region(216,23,932,661)



battle = Battle(tela_toda)