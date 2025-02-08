#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@project-description: This is a simple tank war game created using Pygame and Pymunk.
@file-name: tank.py
@author: PythonDeveloper29042
@author-email: pythondeveloper.29042@outlook.com
@project: TankWarGame
@github-repo: https://github.com/PythonDeveloper29042/TankWarGame.git
@commit-date: 2025-02-08
@description: This file contains the Tank class, which is used to create the tank in the game.
"""
import pygame
from math import sin, cos, tan, pi

import pymunk


class Tank(pygame.sprite.Sprite):
    def __init__(self, name: str, image: str, pos: tuple):
        """This method is used to initialize the Tank object.
        Args:
            image (str): The path of the image of the tank.
        """
        super().__init__()
        self.name = name
        self.image_origin = pygame.image.load(image).convert_alpha()
        self.image = self.image_origin.copy()
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos
        self.direction = 0
        # Boolean flags to check if the tank has turned left or right
        self.turn_left = False
        self.turn_right = False
        # Boolean flags to check if the tank is moving forward or backward
        self.move_forward = False
        self.move_backward = False
        self.clock = pygame.time.Clock()
        self.speed = 2
        # Set the tank
        self.body = pymunk.Body(1, 1, body_type=pymunk.Body.DYNAMIC)
        self.body.position = self.pos
        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
        self.shape.elasticity = 0.5
        self.shape.collision_type = 1

    def shoot(self):
        """This method is used to shoot the tank."""
        pass

    def destroy(self):
        """This method is used to destroy the tank."""
        pass

    def move(self, direction: int):
        """This method is used to move the tank.
        Args:
            direction (int): The direction in which the tank should move. 1 for forward, 2 for backward.
        """
        # Calculate the speed of the tank in the x and y directions
        x_speed = self.speed * sin(self.direction / 180 * pi)
        y_speed = self.speed * cos(self.direction / 180 * pi)
        pos_x, pos_y = self.body.position  # Get the position of the tank
        # Move the tank forward
        if direction == 1:
            pos_x += x_speed
            pos_y += y_speed
        # Move the tank backward
        if direction == 2:
            pos_x -= x_speed
            pos_y -= y_speed
        self.body.position = (pos_x, pos_y)  # Set the new position of the tank

    def rotate(self, direction: int):
        """ This method is used to rotate the tank to a specific direction.
        Args:
            direction (int): The direction in which the tank should turn. 1 for left, 2 for right.
        """
        self.clock.tick(60)  # Set the frame rate
        if direction == 1:  # Rotate left
            self.direction += 1
        if direction == 2:  # Rotate right
            self.direction -= 1
        self.direction %= 360  # Normalize the direction
        self.image = pygame.transform.rotate(self.image_origin, self.direction)  # Rotate the image

        old_center = self.rect.center  # Get the old center of the tank

        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def show(self, screen: pygame.Surface):
        """This method is used to show the tank on the screen.
        Args:
            screen (pygame.Surface): The screen to show the tank.
        """
        screen.blit(self.image, self.rect)

    def update(self, *args, **kwargs):
        """
        This method is used to update the tank.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if self.turn_left: 
            self.rotate(1)  
        if self.turn_right:
            self.rotate(2)
        if self.move_forward: 
            self.move(1)    
        if self.move_backward: 
            self.move(2)
        self.rect.center = self.body.position  # Set the center of the tank to the position of the tank