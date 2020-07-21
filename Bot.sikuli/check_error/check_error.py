import sys
mySikuliPath = "C:\\Sikulix\\BotDO\\Bot.sikuli\\"
if not mySikuliPath in sys.path: sys.path.append(mySikuliPath)

from sikuli.Sikuli import *
from java.awt import Robot
import re

class CheckError:
    def __init__(self):
        print("Check Error")
        
    def clean_chat(self):
        click(Pattern("images/check_error/1593972303685.png").targetOffset(-655,37))
        type("/clear")
        type(Key.ENTER)


    def check_chat(self):
        if exists(Pattern("images/check_error/1593974580043.png").similar(0.59)):
            click(Pattern("images/check_error/1593972303685.png").targetOffset(-655,37))
            type("Ai!")
            type(Key.ENTER)
        
        
        

    def sacola_viagem(self):
        if Region(212,640,277,128).exists("images/check_error/1593886301433.png",2):
            #fix error
            self.clean_chat()


    def disconect(self):
        if Region(472,296,437,195).exists("images/check_error/1593887737569.png",1.5):
            #AJEITAR AINDA
            pass
