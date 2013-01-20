import os, sys #for cls() and exit()
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

