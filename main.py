#!/usr/bin/env python3.3

import Actor, Aui, World, Item
from os import system

def main():
    title_menu =Aui.Menu(logo(),[('1', 'NEW GAME', (new_game, None))])
    current_menu = title_menu
    current_menu.display() 
    main.selected_option = current_menu.retrieve_selection()  

    while main.selected_option  != 'q':
        current_menu = main.selected_option[0](main.selected_option[1]) if main.selected_option != 'q' else current_menu
        current_menu.display() if main.selected_option != 'q' else current_menu
        main.selected_option = current_menu.retrieve_selection() if main.selected_option != 'q' else current_menu

def move(direction):
    while main.player.is_legal_move(direction) != True:
        print('invalid move.')
        direction = input('Try again: ')  
    if direction == 'q':
        main.selected_option = 'q'
        return 'q'
    main.player.move(direction)
    return main.handle_movement_menu

def new_game(*args):
    system('cls')
    main.current_world = World.World()
    main.potion = Item.Item(name='Health Potion', description='Made by 4 loko', image='     4LOKO_ _ _')
    main.current_world.add_item(main.potion, (2,2))
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
