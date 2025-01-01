#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
from pygame.surface import Surface
from pygame import image

# Import sys and os modules for importing a module in parent directory
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of the file.
parent_dir = os.path.dirname(current_dir)  # Get the parent directory of the current directory.
sys.path.append(parent_dir)  # Append the parent directory to the system path.

from constants import MAP_IMAGE_WIDTH, MAP_IMAGE_HEIGHT  # Import the MAP_IMAGE_WIDTH and MAP_IMAGE_HEIGHT constants from the constants module in the parent directory.


class Map:
    def __init__(self, data, screen: Surface):
        """
        This method initializes the Map object.
        Args:
            data: The data of the map.
            screen: The screen to display the map.
        """
        self.data = data
        self.screen = screen
        self.map_tiles = []
        self.load_images()

    def load_images(self):
        """This method loads the images of the map."""
        self.map_tiles.clear()
        for i in range(len(self.data)):
            t = []
            for j in range(len(self.data[i])):
                t.append(image.load(f"./assets/images/Default size/{self.data[i][j]}.png"))
            self.map_tiles.append(t) 

    def show(self):
        """This method displays the map on the screen."""
        for i in range(len(self.map_tiles)):
            for j in range(len(self.map_tiles[i])):
                x = MAP_IMAGE_WIDTH * j
                y = MAP_IMAGE_HEIGHT * i
                self.screen.blit(self.map_tiles[i][j], (x, y))

