class World:
    def __init__(self, name='DEFAULT WORLD', size=[4,4], description='NO DESCRIPTION'):
        # World Attributes:
            # name: string
            # size: [width, height]
            # description: string
            # coordinates: dictionary {(x,y): tile}
            # width: size[0]
            # height: size[1]
            # entity: [[x,y],entity]

        self.name = name
        self.size = size
        renderer = 0
        self.description = description
        self.coordinates = {}
        self.width = size[0]
        self.height =  size[1]
        self.entities = []
        self.empty_tile = '|     |     |_ _ _'

        # Populate self.coordinates{} dictionary with coordinates of range self.size[x,y]. Coordinates are paired with an ascii block reference for the value.
        for x in range(self.width):
            for y in range(self.height):
                self.coordinates[x,y] = self.empty_tile # Empty tile with grid lines.
                y +=1
            x+=1

        self.coordinates_original = dict(self.coordinates)
        # Will eventually be the map file, and will replace
        #  the empty populate method.

    def add_to_map(self, entity):
        self.entities.append(entity)
        self.coordinates[entity.location[0],entity.location[1]] = entity.tile
        entity.current_world = self
        self.update()

    def update(self):
        for entity in self.entities:
            self.coordinates[entity.location[0],entity.location[1]] = entity.tile

    def remove_from_map(self, entiy):
        self.coordinates[entity.location[0],entity.location[1]] = self.coordinates_original[entity.location[0],entity.location[1]]
        self.entities.remove(entity)

    #DEBUG FUNCTION
    def display_coordinates(self):
        x = list(self.coordinates)
        x.sort()
        display = "{} coordinates total.\n".format(len(self.coordinates))
        for i in range (len(self.coordinates)):
            display += "{}: {}\n".format(x[i], self.coordinates[x[i]])
        return display

##class Tile:
##    tiles = ()
##    def __init__(self, name='EMPTY', tile_face='|     |     |_ _ _'):
##        Tile.tiles += (name, tile_face)
##
##        self.name = name
##        self.tile_face = tile_face
##
##    @staticmethod
##    def get_list():
##        return Tile.tiles

#Create Tiles:
# EMPTY = Tile()
#'|     '
#'|     '
#'|_ _ _'

# PLAYER = Tile('PLAYER', '|     |  P  |_ _ _')
#'|     '
#'|  P  '
#'|_ _ _'

def test(): # Master test - Success!
    #World Test
    test_world = World()
    print ('Creating default world:')
    print ("\
Debug info:\n \
  World: {}\n \
  Size: {} - \
Width: {} - \
Height: {} \n\n\
  Description: {}\n\n \
Coordinates: {}\n\n".format(test_world.name,
                                test_world.size,
                                test_world.width,
                                test_world.height,
                                test_world.description,
                                test_world.display_coordinates()))

    #Tile Test
    print ('List of tiles(',len(Tile.tiles),' total):')
    for tile in Tile.get_list():
        print (tile)
