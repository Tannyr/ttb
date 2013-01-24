#!/usr/bin/env python
class World:
    def __init__(self, name='DEFAULT WORLD', size=[4,4], description='NO DESCRIPTION'):
        self.name = name
        self.description = description
        self.coordinates = {}
        self.entities = []
        self.size = size
        self.width = size[0]
        self.height =  size[1]
        
        self.renderer = 0
        self.empty_tile = '|     |     |_ _ _'

        self.populate_world(self.empty_tile)
        self.coordinates_original = dict(self.coordinates)

    def add_entity(self, entity):
        self.entities.append(entity)
        self.update_entity(entity)
        entity.current_world = self
        self.update()

    def update_original_world(self, location, tile):
        self.coordinates_original[location] = tile

    def update(self):
        for entity in self.entities:
            self.update_entity(entity)

    def revert_old_location(self, entity):
        old_x = entity.old_location[0]
        old_y = entity.old_location[1]
        new_x = entity.location[0]
        new_y = entity.location[1]
        
        self.coordinates[old_x,old_y] = \
        self.coordinates_original[new_x,new_y]

    def remove_entity(self, entiy):
        e_x = entity.location[0]
        e_y = entity.location[1]
        
        self.coordinates[e_x,e_y] = self.coordinates_original[e_x,e_y]
        self.entities.remove(entity)

    # ABSTRACTION FUNCTIONS
    def populate_world(self, tile='|     |     |_ _ _'):
        for x in range(self.width):
            for y in range(self.height):
                self.coordinates[x,y] = tile
                y +=1
            x+=1

    def is_empty(self, location):
        if location in self.coordinates:
            return True
        else:
            return False

    def update_entity(self, entity):
        e_x = entity.location[0]
        e_y = entity.location[1]
        
        self.coordinates[e_x,e_y] = entity.tile

    # TEST / DEBUG FUNCTIONS
    def display_coordinates(self):
        x = list(self.coordinates)
        x.sort()
        display = "{} coordinates total.\n".format(len(self.coordinates))
        for i in range (len(self.coordinates)):
            display += "{}: {}\n".format(x[i], self.coordinates[x[i]])
        return display


