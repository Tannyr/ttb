#!/usr/bin/env python
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


screen = Age.Graphics()
test_map = World.World('Test Map', [8,6], 'Test map')
player = Actor.Actor(name='Player 1', tile='|     |  P  |_ _ _')

test_map.add_entity(player)
screen.render(test_map)
command = 0
while command != 'q':
    command = input('ENTER MOVEMENT COMMAND(wsad,(q)uit):')
    if command in  ['w','s','a','d']:
        os.system('cls')
        player.move(command)       
    elif command == 'q':
        pass
    else:
        print('Invalid Command')


