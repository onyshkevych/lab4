class Park:
    def __init__(self, name, description = None, character = None, item = None, friend = None):
        self.name = name
        self.description = description
        self.napriamok = {}
        self.character = character
        self.item = item
        self.friend = friend
    def set_description(self, povidomlennia):
        self.description = povidomlennia
    def link_location(self,other, vector: str):
        self.napriamok[other] = vector
    def set_character(self, character):
        self.character = character
    def set_item(self, item):
        self.item = item
    # def set_friend(self, friend):
    #     self.friend = friend     
    def get_details(self):
        print (self.name)
        print ("--------------------")
        print (self.description)
        print ()
    def get_character(self):
        return self.character
    def get_item(self):
        return self.item
    def move(self, command):
        move = [location for location, value in self.napriamok.items() if value == command]
        for i in move:
            return i
peremohy = 0        
class Enemy:
    peremohy = 0
    def __init__(self, name, enemy):
        self.name = name
        self.enemy = enemy
    def set_conversation(self, conversation):
        self.conversation = conversation
    def set_weakness(self, weakness):
        self.weakness = weakness
    def describe(self):
        print (f"{self.name} є тут! \n{self.enemy}")
    def talk(self):
        print (f"[{self.name} каже]: {self.conversation}")
    peremohy = []    
    def fight(self, fight_with):
        if fight_with == self.weakness:
            print (f"Ви відбили {self.name} з {self.enemy}")
            return True
        else:
            print (f"{self.name} перемігає тебе, невдахо!")
    def get_defeated(self):
        global peremohy
        peremohy += 1
        return peremohy
class Item:
    def __init__(self,item = None, description = None):
        self.item = item
        self.desccription = description
    def set_description(self, description):
        self.desccription = description
    def get_name(self):
        return self.item
    def describe(self):
        print (f"[{self.item}] є тут - {self.desccription}")
class Friend:
    def __init__(self, name, description = None, rich = []):
        self.name = name
        self.description = description
        self.rich = rich
    def set_description(self, description):
        self.description = description
    def get_name(self):
        return self.name
    def describe(self):
        print (f"{self.name} може підтримати тебе {self.description}")
    def help(self):
        print("Я тобі допоможу.")          