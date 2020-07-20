class Tela:
    def __init__(self):
        self.action_screen = self.get_action_screen_position()
        self.left_border = None
        self.top_border = None
        self.right_border = None
        self.botton_border = None
        self.get_borders_position()
        self.top_border.highlight(1)
        self.battle_detect()

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

    def battle_detect(self):
        onAppear("1594766090257.png", self.start_battle) # or any other onXYZ()
        observeInBackground()

    def start_battle(self,event):
        if event.isAppear():
            self.battle = Battle()