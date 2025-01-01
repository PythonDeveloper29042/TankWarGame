#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@file-name: tank.py
@description: This file contains the Tank class, which is used to create the tank in the game.

"""
import pygame
from math import sin, cos, tan, pi


class Tank(pygame.sprite.Sprite):
    def __init__(self, image: str, pos: tuple):
        """This method is used to initialize the Tank object.
        Args:
            image (str): The path of the image of the tank.
        """
        super().__init__()
        self.image_origin = pygame.image.load(image).convert_alpha()
        self.image = self.image_origin.copy()
        self.rect = self.image.get_rect()
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
        # Move the tank forward
        if direction == 1:
            self.rect.centerx += x_speed
            self.rect.centery += y_speed
        # Move the tank backward
        if direction == 2:
            self.rect.centerx -= x_speed
            self.rect.centery -= y_speed

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