#!/usr/bin/env python3.3
import Age, World, Actor, os

# Current Goal:
# *******************************
# THE LEGEND OF TANNYR THE BADASS
# *******************************
# Start Menu:
# -New Game
# --8x8 grid, moveable player, collision detection.
# --Win status: Picks up item and inspects it.
# -Load Game
# --Loads map with world-entities locations saved.
# -Exit
# --Closes Window

# Future goals:
# Remove [enter] key neccesity and add refresh rate,
# Increase movement resolution of grid.




def main():
    screen = Age.Graphics()
    test_map = World.World('Test Map', [10,3], 'Test map')
    player = Actor.Actor(name='Tannyr', health = 100, tile='|     |  P  |_ _ _', inventory = ['Sword', 'Shield'])
    
    test_map.add_entity(player)
    # First loop kickoff
    screen.render(test_map)
    player.ui()
    command = None

    while command != 'q':
        command = input('ENTER MOVEMENT COMMAND(wsad,(q)uit):')
        if command in  ['w','s','a','d']:
            player.move(command)
        elif command == 'q':
            pass
        else:
            print('Invalid Command')



main()
