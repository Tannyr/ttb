import World #Only used in render_debug(), not dependant.

#TODO: Fix grid, height is of by one.  Write debug function that populates each grid space with its coordinate
class Graphics:
    # Graphics engine.  Anything that is seen will submit info to this for rendering.
    # Recieves objects to print to screen, and handles output.
    # Attributes: coordinates, coordinate_changes
    def __init__(self):
        self.coordinates = {} # Info used to render map.
        self.coordinate_changes = {} # Changes to map.  Requires update() to utilize.
    
    def render(self, world): #Outputs display using coordinates dictionary.
        world.renderer = self
        top_row, middle_row, bottom_row = (0,6), (6,12), (12,18)
        display = ""

        #Render and print display
        display += " {}\n".format('_ _ _ '* world.width) # Top of display

        # (grid-height) times do => (row-height) times do => (grid-width_ times do
        # => append correct part of current coordinates tile. Append '|' at the end of each row.
        
        for y in range(world.height):
            for z in range(3):
                for x in range(world.width):
                    if z == 0:
                        display += world.coordinates[x,y][top_row[0]:top_row[1]]
                    elif z == 1:
                        display += world.coordinates[x,y][middle_row[0]:middle_row[1]]
                    elif z == 2:
                        display += world.coordinates[x,y][bottom_row[0]:bottom_row[1]]
                    else:
                        print ("SOMETHING WENT WRONG")
                    if x == world.width-1:
                        display += "|\n"
                            
        print (display)
        #Sample Grid
        # _ _ _ _ _ _ 
        #|     |     |
        #| 0,0 | 1,0 |
        #|_ _ _|_ _ _|
        #|     |     |
        #| 0,1 | 1,1 |
        #|_ _ _|_ _ _|
            
    def render_debug(self, world = World.World('Test Map', [8,6], 'Test map')):
    # Renders map and all it's info.
        print ("World: {}\n \
                {}\n \
                Debug info:\n \
                Size: {}\n \
                Description:{}\n \
                Features: {}\n \
                Coordinates: {}".format(world.name,
                                        self.render(world),
                                        world.size,
                                        world.description,
                                        world.coordinates)) #index out of range error

    def update(self): #updates coordinates dictionary with what is stored in world_changes.
        self.coordinates = dict(list(self.coordinates.items()) + list(self.coordinate_changes.items()))
        self.coordinate_changes = {}


def test():
    screen = Graphics()
    world = World.World('Test Map', [8,6], 'Test map')
    print (world.display_coordinates())
            
    
