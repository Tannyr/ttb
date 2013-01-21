#!/usr/bin/env python
import os

class Actor:
    def __init__(self, name='Default', gender='m', inventory=[], health=0, tile='|     |     |_ _ _'):
        self.name = name
        self.gender = gender
        self.inventory=inventory
        self.health=health
        self.location = [0,0]
        self.current_world = 0
        self.tile = tile
        self.old_location = list(self.location)
        
    # PRIMARY METHODS
    def move(self, direction):
        UP = 'w'
        RIGHT = 'd'
        DOWN = 's'
        LEFT = 'a'
        self.save_old_location()
        
        if direction == UP:
            new_coord = self.location[0],self.location[1]-1 
            if self.current_world.is_empty(new_coord):
                self.location[1] -=1
            else:
                print ('Invalid move.')
                return 
        elif direction == DOWN:
            new_coord = self.location[0],self.location[1]+1             
            if self.current_world.is_empty(new_coord):
                self.location[1] +=1
            else:
                print ('Invalid move.')
                return
        elif direction == RIGHT:
            new_coord = self.location[0],self.location[0]+1             
            if self.current_world.is_empty(new_coord):
                self.location[0] +=1
            else:
                print ('Invalid move.')
                return
        elif direction ==LEFT:
            new_coord = self.location[0],self.location[0]-1             
            if self.current_world.is_empty(new_coord):
                self.location[0] -=1
            else:
                print ('Invalid move.')
                return
        else:
            print ('Invalid move due to programmer error.  Nice job, guy.')
        self.current_world.revert_old_location(self)
        self.current_world.update()
        os.system('cls')
        self.call_for_render()
        self.ui()

    def list_inventory(self):
        item_list = ''
        for item in self.inventory:
            item_list += '{}, '.format(item)
            if item == self.inventory[-1]:
                item_list = item_list[0:-2]
        return item_list

    def ui(self):
        print ("{}\n HEALTH: {}\n INVENTORY: {}\n".format(self.name, self.health, self.list_inventory() ))
        # Player
        # HEALTH: 0
        # INVENTORY: Bat, Ball, Barbell.

    # ABSRACTION METHODS
    def save_old_location(self):
        self.old_location = list(self.location)

    def call_for_render(self):
        self.current_world.renderer.render(self.current_world)
        
        


