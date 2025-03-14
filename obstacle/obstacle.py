#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
@project-description: This is a simple tank war game created using Pygame and Pymunk libraries.
@file-name: obstacle.py
@author: PythonDeveloper29042
@author-email: pythondeveloper.29042@outlook.com
@project: TankWarGame
@github-repo: https://github.com/PythonDeveloper29042/TankWarGame.git
@commit-date: 2025-02-08
@description: This file contains the Obstacle class, which is used to create the obstacles in the game.

"""

import pygame
from pygame.locals import *
import pymunk


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image: str, direction: int, pos: tuple):
        """Initializes the obstacle class.
        Args:
            image (str): The image of the obstacle.
            direction (int): The direction of the obstacle.
            pos (tuple): The position of the obstacle.
        """
        super().__init__()  # Initialize the Sprite class.
        self.direction = direction  # The direction of the obstacle.
        self.image = pygame.image.load(
            image
        ).convert_alpha()  # Get the image of the obstacle.
        self.image = pygame.transform.rotate(
            self.image, self.direction
        )  # Rotate the image.
        self.rect = self.image.get_rect()  # Get the rectangle of the image.
        # Set the position of the obstacle.
        self.pos = pos
        self.rect.center = pos
        # Set the physical effects of the obstacle.
        self.body = pymunk.Body(1, 1, body_type=pymunk.Body.STATIC)
        self.body.position = self.pos
        self.body.angle = self.direction  # Angle of the obstacle.
        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
        self.shape.elasticity = 1.0
        self.shape.collision_type = 2

    def show(self, screen: pygame.Surface):
        """Shows the obstacle on the screen.
        Args:
            screen (pygame.Surface): The screen to show the obstacle.
        """
        screen.blit(self.image, self.rect)
