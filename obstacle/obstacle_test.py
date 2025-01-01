import pygame
from obstacle import Obstacle
import sys, os  # Import sys and os modules for importing a module in parent directory

current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of the file.
parent_dir = os.path.dirname(current_dir)  # Get the parent directory of the current directory.
sys.path.append(parent_dir)  # Append the parent directory to the system path.

from level import *

pygame.init()
screen = pygame.display.set_mode((918, 515))
images = read_map("../config.json")
obstacle_ = read_obstacle("../config.json")
objs = []  # List to store the objects.
for obs in obstacle_:
    for p in obs["pos"]:
        temp = Obstacle(f"../assets/images/Default size/{obs["path"]}.png", p[-1], p[:2])
        objs.append(temp)

while True:
    for obj in objs:
        obj.show(screen)
    pygame.display.update()