import World

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

    def move_up(self):
        self.location[1] -=1

    def move_down(self):
        self.location[1] +=1

    def move_left(self):
        self.location[0] -=1

    def move_right(self):
        self.old_location = self.location[0],self.location[1]
        self.location[0] +=1
        self.current_world.coordinates[self.old_location[0],self.old_location[1]] = self.current_world.coordinates_original[self.location[0],self.location[1]]
        self.current_world.update()
        self.current_world.renderer.render(self.current_world)
        
        


