import pygame
from background import Map
import sys, os  # Import sys and os modules for importing a module in parent directory

current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of the file.
parent_dir = os.path.dirname(current_dir)  # Get the parent directory of the current directory.
sys.path.append(parent_dir)  # Append the parent directory to the system path.

from level import *

pygame.init()
screen = pygame.display.set_mode((918, 515))
images = read_map("../assets/config.json")
map_ = Map(images,screen)

while True:
    map_.show()
    pygame.display.update()