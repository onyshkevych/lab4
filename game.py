class Room:
    def __init__(self, name, description = None, character = None, item = None):
        self.name = name
        self.description = description
        self.napriamok = {}
        self.character = character
        self.item = item
    def set_description(self, povidomlennia):
        self.description = povidomlennia
    def link_room(self,other, vector: str):
        self.napriamok[vector] = other
    def set_character(self, character):
        self.character = character
    def set_item(self, item):
        self.item = item       
    def get_details(self):
        print (self.name)
        print ("--------------------")
        print (self.description)
        for value, room in self.napriamok.items():
            print (f"The {room}" is {value})
    def get_character(self):
        return self.character
    def get_item(self):
        return self.item
    def move(self, command):
        move = [room for value, room in self.napriamok.items() if value == command]
        for i in move:
            return i
peremohy = 0        
class Enemy:
    def __init__(self, name, enemy):
        self.name = name
        self.enemy = enemy
    def set_conversation(self, conversation):
        self.conversation = conversation
    def set_weakness(self, weakness):
        self.weakness = weakness
    def describe(self):
        print (f"{self.name} is here! \n{self.enemy}")
    def talk(self):
        print (f"[{self.name} says]: {self.conversation}")
    peremohy = []    
    def fight(self, fight_with):
        if fight_with == self.weakness:
            print (f"You fend {self.name} off with the {fight_with}")
            return True
        else:
            print (f"{self.name} crushes you, puny adventurer!")
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
        print (f"The [{self.item}] is here - {self.desccription}")