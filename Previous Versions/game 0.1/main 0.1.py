#Term Key: NI = Not implemented.
#TODO:
#   Create Tileset class and implement.
#   Complete render.
#   Create game prompt loop.
#   Create menu class with attributes: Title, Options.

import os, sys #for cls() and exit()


class Actor:
    def __init__(self, name='Default', gender='m', inventory=[], health=0):
        self.name = name
        self.gender = gender
        self.inventory=inventory
        self.health=health

class Item:
    def __init__(self, name='Default', description='Default', image=0):
        self.name, self.description, self.image = name, description, image

class Map:
    def __init__(self, name='Default Map', size=[], tileset='Default', description='Default map description', features={}):
        self.name = name
        self.size = size
        #self.tileset = tileset
        self.description = description
        self.features = features
        self.width = size[0]
        self.height = size[1]
        self.coordinates = {}
        for x in range(self.width):
            for y in range(self.height):
                self.coordinates[x,y] = "empty"
                y +=1
            x+=1

    def update(self): #doesn't work
        for key, value in self.features:
            self.coordinates[key] = valeu
            
    def render(self):
        x_counter = 0
        y_counter = 0
        
        map = ""
        map += ' ' + '_ _ _ ' *(self.width) + "\n"
        while y_counter < self.height:
            map += ('|{}'.format("     ") * self.width) + "|" + "\n"
            map +=('|{}'.format("  " + str(x_counter) + "  ") * self.width) + "|" + "\n"
            map += '|{}'.format ("_ _ _") * (self.width) + "|" + "\n"
            x_counter +=1
            y_counter +=1
        return map
            
    def render_debug(self):
    # Dummy response
    # Should render map name, then ascii map of appropriate size, then populate it with features.
    # Tileset will EVENTUALLY alter default map legend.
        print ("Map: {}\n{}\nDebug info:\nSize: {}\nDescription:{}\nFeatures: {}\nCoordinates: {}".format(self.name, self.render(), self.size, self.description, self.features, self.coordinates))
        
class Menu:
    def __init__(self, title = 'Default Title', options = {}):
        self.title = title
        self.options = options

    def handle_selection(self, selection):
        self.selection = int(selection)
        return self.options[self.selection -1][1]() #calls selected values corresponding function
        

def title_screen():
    return '''
    *******************************
    THE LEGEND OF TANNYR THE BADASS
    *******************************
    '''

def new_game():
    #map_1.features[(0,0)] = "tannyr"   #clears coord table for some reason
    map_1.render_debug()
    map_1.update()
    return first_menu

def load_game():
    print("You have selected load game.")
    return start_menu

def exit_game():
    sys.exit()

start_menu = Menu(title_screen(), [('NEW GAME', new_game),('LOAD GAME', load_game), ('QUIT', exit_game)])
first_menu = Menu('Options', [('MOVE', new_game),('LOOK', new_game), ('FIND', new_game)])

map_1 = Map('Map 1', [8,8], 'Default', 'My first map!')

potion = Item(name='Health Potion', description='Made by 4 loko', image=0)
player = Actor(name='Tannyr', gender='m', inventory=[potion], health=100)

def main():
    #Pre-loop Setup, clear screen and display title and start menu
    #os.system('cls')
    current_menu = start_menu
    print (current_menu.title)
    for option in current_menu.options:#prints numbered list of options
        print (str(current_menu.options.index(option) + 1) + " - " + str(option[0])) 
    #get line and verify command is legitimate
    acceptable_commands='1','2','3','q'
    command = input('Command: ')
    #os.system('cls')

    #game loop
    game_loop = True
    while game_loop == True:
        while command not in acceptable_commands:
            print (current_menu.title)
            for option in current_menu.options:#prints numbered list of options
                print (str(current_menu.options.index(option) + 1) + " - " + str(option[0])) 
            print('Invalid Command')
            command = input('Command: ')
            #os.system('cls')

        #quit if neccesary
        if command == 'q':
            game_loop = False
            continue

        #handle picked command on current menu, rerender map, and set new current_menu
        current_menu = current_menu.handle_selection(command)
        for option in current_menu.options:
            print (str(current_menu.options.index(option) + 1) + " - " + str(option[0])) 
        command = input('Command: ')
        #os.system('cls')
        
def test():
    screen = Graphics()
    debug_map = World('Debug Map', [8,6], 'My first map!')
    screen.render(debug_map)

#Initialize Game
main()
