import pygame
from tank import Tank
import sys, os  # Import sys and os modules for importing a module in parent directory

current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of the file.
parent_dir = os.path.dirname(current_dir)  # Get the parent directory of the current directory.
sys.path.append(parent_dir)  # Append the parent directory to the system path.

from level import *

pygame.init()
screen = pygame.display.set_mode((918, 515))
images = read_map("../config.json")
tank_data = read_tank("../config.json")
objs = []  # List to store the objects.
for tank in tank_data:
    temp = Tank(f"../assets/images/Default size/{tank['image']}.png", tank["pos"])
    objs.append(temp)

while True:
    for obj in objs:
        obj.show(screen)
    pygame.display.update()