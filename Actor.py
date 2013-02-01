#!/usr/bin/env python
from os import system

class Actor:
    def __init__(self, name='Default', inventory=[], health=0, tile='          _ _ _'):

        # Attributes
        self.UP = 'w'
        self.RIGHT = 'd'
        self.DOWN = 's'
        self.LEFT = 'a'
        self.name = name
        self.inventory=inventory
        self.health=health
        self.location = 0,0
        self.current_world = 0
        self.tile = tile
        
    def list_inventory(self):
        item_list = ''
        for item in self.inventory:
            item_list += '{}, '.format(item)
            if item == self.inventory[-1]:
                item_list = item_list[0:-2]
        return item_list

    #WORLD INTERACTION METHODS
    def move(self, direction):
        x = self.location[0]
        y = self.location[1]
        
        if direction == self.UP:
            new_coord = x, y-1 
        elif direction == self.DOWN:
            new_coord = x, y+1             
        elif direction == self.RIGHT:
            new_coord = x+1, y           
        elif direction == self.LEFT:
            new_coord = x-1, y
        self.move_to_location(new_coord)           
        system('cls')
        
        self.ui()
        self.__request_render()

    def join_world(self, world):
        self.current_world = world
        self.__add_to_new_location(self.location)

    def leave_world(self, world):
        x = self.location[0]
        y = self.location[1]        
        world.coordinates[x,y] = self.coordinates_original[x,y]

    def move_to_location(self, new_location):
        self.__remove_from_old_location(self.location)
        self.__add_to_new_location(new_location)
        self.location = new_location

    def ui(self):
        print ("{}\n HEALTH: {}\t INVENTORY: {}\n"
               .format(self.name, self.health, self.list_inventory() ))    
        
    def __remove_from_old_location(self, location):      
        self.current_world.coordinates[location[0],location[1]] = self.current_world.coordinates_original[location[0],location[1]]

    def __add_to_new_location(self, location):
        self.current_world.coordinates[location[0],location[1]] = self.tile

    def is_legal_move(self, direction):
        x,y = self.location
        if direction == self.UP:
            new_coord = x, y-1 
        elif direction == self.DOWN:
            new_coord = x, y+1
        elif direction == self.RIGHT:
            new_coord = x+1, y           
        elif direction ==self.LEFT:
            new_coord = x-1, y
        elif direction == 'q':
            new_coord = 'q'
        if new_coord in self.current_world.coordinates or new_coord =='q':
            return True
        else:
            return False

    def __request_render(self):
        self.current_world.render()
        
        


