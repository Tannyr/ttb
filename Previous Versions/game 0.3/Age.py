class Graphics:
    def __init__(self):
        pass
    
    def render(self, world):
        world.renderer = self
        top_row, middle_row, bottom_row = (0,6), (6,12), (12,18)
        display = ""

        display += " {}\n".format('_ _ _ '* world.width) # Top of display
        
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
