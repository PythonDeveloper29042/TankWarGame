#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project-description: This is a simple tank war game created using the Pygame and Pymunk libraries.
@file-name: main.py
@author: PythonDeveloper29042
@author-email: pythondeveloper.29042@outlook.com
@project: TankWarGame
@github-repo: https://github.com/PythonDeveloper29042/TankWarGame.git
@commit-date: 
@description: This file contains the main function of the game.
"""

import pygame  # Import the pygame module for the game engine.
import pymunk  # Import the pymunk module for the physics engine.
from pygame.locals import *  # Import the pygame.locals module for the constants of the game.

# from tank.tank import Tank
# from obstacle import Obstacle
# from weapon import Weapon
# from collide import Collide
# from constants import *
from map.background import Map
from obstacle.obstacle import Obstacle
from tank.tank import Tank
from level import *


class TankMain:
    def __init__(self):
        pygame.init()  # Initialize the pygame module.
        self.screen = pygame.display.set_mode((918, 515))  # Set the screen size.
        self.running = True  # Set the running flag to True.
        map_data = read_map("./config.json")  # Read the map data from the config file.
        self.obstacle_data = read_obstacle("./config.json")
        self.tank_data = read_tank("./config.json")

        self.map_obj = Map(
            map_data, self.screen
        )  # Create an instance of the Map class.
        self.obstacle_group = pygame.sprite.Group()  # Create a group for the obstacles.
        self.tank_group = pygame.sprite.Group()  # Create a group for the tanks.



        self.clock = (
            pygame.time.Clock()
        )  # Create a clock object for the game to control the frame rate.

        # Create a space object for the physics engine.
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.create_obstacle()  # Create the obstacles in the game.
        self.create_tank()  # Create the tank in the game.

        self.fps = 60  # Set the frame rate of the game.

        # Create the boundaries of the game.
        line_pos = [[(0, 0), (918, 0)], [(918, 0), (918, 515)], [(918, 515), (0, 515)], [(0, 515), (0, 0)]]
        for pos in line_pos:
            line_body = pymunk.Body(10, 10, body_type=pymunk.Body.STATIC)
            line_shape = pymunk.Segment(line_body, pos[0], pos[1], radius=30)
            line_shape.elasticity = 1.0
            self.space.add(line_body, line_shape)

    def create_obstacle(self):
        """This function creates the obstacles in the game."""
        for obs in self.obstacle_data:
            for p in obs["pos"]:
                temp = Obstacle(
                    f"./assets/images/Default size/{obs['path']}.png", p[-1], p[:2]
                )
                self.obstacle_group.add(temp)
                self.space.add(temp.body, temp.shape)

    def create_tank(self):
        """This function creates the tank in the game."""
        self.tank1 = Tank(
            f"./assets/images/Default size/{self.tank_data[0]['image']}.png",
            self.tank_data[0]["pos"],
        )
        self.tank2 = Tank(
            f"./assets/images/Default size/{self.tank_data[1]['image']}.png",
            self.tank_data[1]["pos"],
        )
        self.tank_group.add(self.tank1)
        self.tank_group.add(self.tank2)
        self.space.add(self.tank1.body, self.tank1.shape)
        self.space.add(self.tank2.body, self.tank2.shape)

    def event_handle(self):
        """This function handles the events in the game."""
        for e in pygame.event.get():  # Get the events from the pygame module.
            if (
                e.type == QUIT
            ):  # If the event is QUIT, then set the running flag to False
                self.running = False
            if (
                e.type == KEYDOWN
            ):  # If the event is KEYDOWN, then check the key pressed.
                if (
                    e.key == K_a
                ):  # If the key pressed is 'a', then set the turn_left flag of tank1 to True.
                    self.tank1.turn_left = True
                if (
                    e.key == K_d
                ):  # If the key pressed is 'd', then set the turn_right flag of tank1 to True.
                    self.tank1.turn_right = True
                if (
                    e.key == K_LEFT
                ):  # If the key pressed is 'LEFT', then set the turn_left flag of tank2 to True.
                    self.tank2.turn_left = True
                if (
                    e.key == K_RIGHT
                ):  # If the key pressed is 'RIGHT', then set the turn_right flag of tank2 to True.
                    self.tank2.turn_right = True
                if (
                    e.key == K_w    
                ):  # If the key pressed is 'w', then set the move_forward flag of tank1 to True.
                    self.tank1.move_forward = True
                if (
                    e.key == K_s
                ):  # If the key pressed is 's', then set the move_backward flag of tank1 to True.
                    self.tank1.move_backward = True
                if (
                    e.key == K_UP
                ):  # If the key pressed is 'UP', then set the move_forward flag of tank2 to True.
                    self.tank2.move_forward = True
                if (
                    e.key == K_DOWN
                ):  # If the key pressed is 'DOWN', then set the move_backward flag of tank2 to True.
                    self.tank2.move_backward = True
            if e.type == KEYUP:  # If the event is KEYUP, then check the key released.
                if (
                    e.key == K_a
                ):  # If the key released is 'a', then set the turn_left flag of tank1 to False.
                    self.tank1.turn_left = False
                if (
                    e.key == K_d
                ):  # If the key released is 'd', then set the turn_right flag of tank1 to False.
                    self.tank1.turn_right = False
                if (
                    e.key == K_LEFT
                ):  # If the key released is 'LEFT', then set the turn_left flag of tank2 to False.
                    self.tank2.turn_left = False
                if (
                    e.key == K_RIGHT
                ):  # If the key released is 'RIGHT', then set the turn_right flag of tank2 to False.
                    self.tank2.turn_right = False
                if (
                    e.key == K_w
                ):  # If the key released is 'w', then set the move_forward flag of tank1 to False.
                    self.tank1.move_forward = False
                if (
                    e.key == K_s
                ):  # If the key released is 's', then set the move_backward flag of tank1 to False.
                    self.tank1.move_backward = False
                if (
                    e.key == K_UP
                ):  # If the key released is 'UP', then set the move_forward flag of tank2 to False.
                    self.tank2.move_forward = False
                if (
                    e.key == K_DOWN
                ):  # If the key released is 'DOWN', then set the move_backward flag of tank2 to False.
                    self.tank2.move_backward = False

    def show(self):
        """This function displays the game on the screen."""
        while self.running:
            self.clock.tick(self.fps)
            self.space.step(1 / self.fps)
            self.event_handle()
            self.map_obj.show()
            self.obstacle_group.draw(self.screen)
            self.tank_group.draw(self.screen)
            self.tank_group.update()
            pygame.display.update()


def main():
    """This is the main function of the game."""
    tank_main = TankMain()  # Create an instance of the TankMain class.
    tank_main.show()  # Call the show method of the TankMain class to display the game.


if __name__ == "__main__":
    main()
