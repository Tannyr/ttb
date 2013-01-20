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
            self.location[1] -=1
        elif direction == DOWN:
            self.location[1] +=1
        elif direction == RIGHT:
            self.location[0] +=1
        elif direction ==LEFT:
            self.location[0] -=1
        else:
            return 'Invalid Selection'
        self.current_world.revert_old_location(self)
        self.current_world.update()
        self.call_for_render()

    # ABSRACTION METHODS
    def save_old_location(self):
        self.old_location = list(self.location)

    def call_for_render(self):
        self.current_world.renderer.render(self.current_world)
        
        


