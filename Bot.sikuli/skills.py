import re
class Skills:
    def __init__(self):
        self.skills = { "martelo_da_lua": {"pa": 6 , "element": 4 , "range_type": "circle", "min_range": 4 , "max_range": 7 , "effect_area": "single_cell" , "delay": 2 , "effects": {"range": -1}, "min_damage": 38 , "max_damage":47, "class": "any"}, 
                                    "furia": {"pa": 3, "element": 4, "range_type": "single_cell", "min_range": 1, "max_range": 1, "effect_area": "single_cell", "min_damage": 30, "max_damage": 34, "round_uses": 3, "target_limit": 2,  "class": "sac" }}
        self.cooldown = {}
        self.tela = Screen()
        self.janela = Region(217,23,932,745)
        self.get_character_skills()
        e = 0.799167533819
        
    def get_character_skill(self, character_class):
        class_skills = {}
        for skill in self.skills:
            if self.skills[skill]["class"] == character_class or self.skills[skill]["class"] == "any" :
                skills.append(skill)

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
                    print change
                    print change.getW()/
                    
        type("c")
                    

skill = Skills() 

# H= 0.80 +/- 0.01 * W
# W= H/0.80+/- 0.01
#d = Region(251,422,171,22)
#a = find("1595968184482.png")
#print a
#Region(a.getX()-25,a.getY()+328,171,22).highlight(5)