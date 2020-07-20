class CheckError:

    def clean_chat(self):
        click(Pattern("1593972303685.png").targetOffset(-655,37))
        type("/clear")
        type(Key.ENTER)


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
