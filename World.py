#!/usr/bin/env python

class World:
    def __init__(self, name= 'DEFAULT WORLD', size= [4,4], description= 'NO DESCRIPTION'):
        empty_tile= '          _ _ _' #15 CHARS
        
        # Attributes
        self.name= name
        self.description= description
        self.coordinates= {}
        self.size= size
        self.width= size[0]
        self.height=  size[1]
        self.items= []

        self.__create_empty_world(empty_tile)
        self.coordinates_original= dict(self.coordinates)

    def add_item(self, item, location):
        self.__add(item, location)
        self.items.append(item)
        
    def __add(self, to_add, where_to_add):
        self.coordinates[where_to_add]= to_add.image
        
    def render(self):
        top_row, middle_row, bottom_row= (0,5), (5,10), (10,15)       
        display= " {}\n".format('_ _ _ '* self.width)
        
        for y in range(self.height):
            for z in range(3):
                for x in range(self.width):
                    display+= "|"
                    if z== 0:
                        display+= self.coordinates[x,y][top_row[0]:top_row[1]]
                    elif z== 1:
                        display+= self.coordinates[x,y][middle_row[0]:middle_row[1]]
                    elif z== 2:
                        display+= self.coordinates[x,y][bottom_row[0]:bottom_row[1]]
                        
                    if x== self.width-1:
                        display += "|\n"
        print (display)

    # Helper Methods
    def __create_empty_world(self, tile):
        for x in range(self.width):
            for y in range(self.height):
                self.coordinates[x,y]= tile
                y+= 1
            x+= 1
            
# Test Functions
def test():
    test = World()
    print ("Test world created! \n \
    World name: {},\t Description: {},\n Size: {},\t Width: {},\t Height: {},\n \
    Renderer: {} \n \n \
    Coordinates: \n \
    {}".format(test.name, test.description, test.size, test.width, test.height, test.renderer, display_coordinates(test)))

def display_coordinates(world):
    x= list(world.coordinates)
    x.sort()
    display= "{} coordinates total.\n".format(len(world.coordinates))
    for i in range (len(world.coordinates)):
        display+= "{}: {}\n".format(x[i], world.coordinates[x[i]])
    return display



