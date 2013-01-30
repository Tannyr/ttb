#!/usr/bin/env python3.3

# Current Goal:
# *******************************
# THE LEGEND OF TANNYR THE BADASS
# *******************************
# Start Menu:
# -New Game
# --10x8 world, moveable player, collision detection. !
# --Win status: Picks up item and inspects it.
# -Load Game
# --Loads map with world-entities locations saved.
# -Exit
# --Closes Window

# Future goals:
# Remove [enter] key neccesity and add refresh rate,
# Increase movement resolution of grid.

import Actor, Aui, World
from os import system

def main():
    title_menu =Aui.Menu(logo(),[('1', 'NEW GAME', (new_game, None))])
    current_menu = title_menu
    current_menu.display() # prints menu's title and options
    main.selected_option = current_menu.retrieve_selection()  

    while main.selected_option != 'q':     
        current_menu = main.selected_option[0](main.selected_option[1]) if main.selected_option[0] != 'q' else current_menu
        current_menu.display()
        main.selected_option = current_menu.retrieve_selection()  

def move(direction):
    while main.player.is_legal_move(direction) != True:
        print('invalid move.')
        direction = input('Try again: ')  
    if direction == 'q':
        main.selected_option = 'q'
        return 'q'
    main.player.move(direction)
    return main.handle_movement_menu
 
    # Main Menu Functions
def new_game(*args):
    system('cls')
    main.current_world = World.World()
    main.player = Actor.Actor('Tannyr', inventory=[], health=100, tile='       P  _ _ _')
    main.player.join_world(main.current_world)
    main.handle_movement_menu = Aui.Menu("Move Player:",[('w', 'UP', (move, 'w')),
                                                     ('s', 'DOWN', (move, 's')),
                                                     ('a', 'LEFT', (move, 'a')),
                                                     ('d', 'RIGHT', (move, 'd'))])
    main.player.ui()
    main.current_world.render()
    
    return main.handle_movement_menu

def logo():
    return '''
                |*******|********|
        |***************|***************|
        |         THE LEGEND OF         |
        |       TANNYR THE BADASS       |
        |***************|***************|
         \\\\\\\\\\         /|\         /////
                      | | |
                      | | |
                      | | |
                      | | |
                      | | |
                   (===(*)===)
                       ( )
                       ( )
                       (_)
    '''

# Helpers
 
main()
