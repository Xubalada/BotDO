import re
class Tela:
    def __init__(self):
        self.screen_size = Screen()
        self.screen_proportion = self.get_screen_proportion()
        self.action_screen_proportion = 0.8
        self.action_screen = self.get_action_screen()
        print self.get_character_status()
        popup("a")
        self.get_character_skills()
        self.left_border = None
        self.top_border = None
        self.right_border = None
        self.botton_border = None
        self.get_borders_position()
        self.battle_detect()

    def get_character_status(self):#ajeitar getw do numero
        click(Region(107,757,35,4))#chat_box
        type("/clear")
        type(Key.ENTER)
        type(Key.ESC)
        my_status = {"vitalidade": Region.text(self.get_status_number_region(findText("Vitalidade"))),
                     "agilidade": Region.text(self.get_status_number_region(findText("Agilidade"))),
                     "sorte": Region.text(self.get_status_number_region(findText("Sorte"))),
                     "forca": Region.text(self.get_status_number_region(findText(ucode("Forca")))),
                     "inteligencia": Region.text(self.get_status_number_region(findText(ucode("Intelig")))),
                     "sabedoria":  Region.text(self.get_status_number_region(findText("Sabedoria")))
                     }
        for status in my_status:
            if my_status[status] == "" or my_status[status] == "-":
                my_status[status] = 0
            else:
                my_status[status] == int(*re.search(r'(\d+)', my_status[status] ))
        print (my_status)
        return my_status
                
    
    def get_status_number_region(self,status_text_region):
        Region(status_text_region.getX()+ int(self.action_screen.getW()*0.12708) ,status_text_region.getCenter().getY() - int(self.action_screen.getH()*0.0325/2), int(self.action_screen.getW()*0.05625) ,int(self.action_screen.getH()*0.0366)).highlight(0.5)
        return Region(status_text_region.getX()+ int(self.action_screen.getW()*0.12708) ,status_text_region.getCenter().getY() - int(self.action_screen.getH()*0.0325/2), int(self.action_screen.getW()*0.05625) ,int(self.action_screen.getH()*0.0366))
        

    def get_character_skills(self):
        self.screen = Finder(Image.create(Pattern(capture(Screen()))))
        self.screen.setFindChangesImageDiff(100)
        type("c")
        wait(1)
        changes = self.screen.findChanges(capture(self.screen))
        for change in changes:
            if change.getW() > 50:
                if change.getH() > 200:
                    change.highlight(1)
                    print self.action_screen  
                    print change
                    print float(change.getW())/self.action_screen.getW(),float(change.getH())/self.action_screen.getH()    
                    a = Region(int(change.getX()+ self.action_screen.getW() * 0.056),int(change.getY()+ self.action_screen.getH() * 0.457),int(self.action_screen.getW()*0.171),int(self.action_screen.getH()*0.0364))
                    Region(a.getX(),a.getY()+ 5*a.getH(),a.getW(),a.getH()).highlight(1)
        type("c")

    def get_screen_proportion(self):
        return float(self.screen_size.getH())/float(self.screen_size.getW())

    def get_action_screen(self):
        if self.screen_proportion <= self.action_screen_proportion:
            x_position = int((self.screen_size.getW() - float(self.screen_size.getH())/self.action_screen_proportion)/2)
            return Region(x_position,0,int(float(self.screen_size.getH())/self.action_screen_proportion),self.screen_size.getH())
        y_position = int((self.screen_size.getH() - float(self.screen_size.getW()) * self.action_screen_proportion)/2)
        return Region(0,y_position, self.screen_size.getW(), int(float(self.screen_size.getW())*self.action_screen_proportion))


    def get_screen_position(self):
        screen_reg = find(capture())    
        return Region(screen_reg.getX(),screen_reg.getY(),screen_reg.getW(),screen_reg.getH())
        
        
    def get_borders_position(self):
        axe_x = self.action_screen.getX()
        axe_y = self.action_screen.getY()
        width = self.action_screen.getW()
        high = self.action_screen.getH()
        self.left_border = Region(axe_x, axe_y, width/100, high)
        self.top_border = Region(axe_x, axe_y, width, high/100)
        self.right_border = Region(axe_x + (width - width/100), axe_y, width/100, high)
        self.botton_border = Region(axe_x,int(high*0.883) - high/100 ,width, high/100)
        
    def get_chat_write_box_position(self):
        popup("Select the chat write box position")
        return self.get_screen_position()

    def battle_detect(self):#incompleto
        onAppear("1594766090257.png", self.start_battle) # or any other onXYZ()
        observeInBackground()

    def start_battle(self,event):
        if event.isAppear():
            self.battle = Battle()
t = Tela()