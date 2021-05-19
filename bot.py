from math import fabs


class bot:
    name = ['isaac']
    BotStatus = True
    isBotawake = False
    def setName(self,name):
        self.name = name
    def setSleep(self):
        self.isBotawake = False
    def awake(self):
        self.isBotawake = True
    def quit(self):
        self.isBotawake = False
        self.BotStatus = False
   