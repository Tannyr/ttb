#!/usr/bin/env python
class Item:
    def __init__(self, name='Default', description='Default', image=0):
        self.name, self.description, self.image = name, description, image


potion = Item(name='Health Potion', description='Made by 4 loko', image=0)
