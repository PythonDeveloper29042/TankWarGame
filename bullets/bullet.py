"""
@description: This module contains the Bullet class.
"""
import pymunk
import pygame  # Import the pygame module.
from pygame.surface import Surface  # Import the Surface class from the pygame module.
from pygame.sprite import Sprite  # Import the Sprite class from the pygame module.
from math import sin, cos, pi as π  # Import the sin, cos, and pi functions from the math module.


# Create the Bullet class.
class Bullet(Sprite):
    def __init__(self, image: Surface, direction: int, pos: tuple):
        """
        Initializes the Bullet class.
        Args:
            image (Surface): The image of the bullet.
            direction (int): The direction of the bullet.
        """
        super().__init__()
        self.count = 0  # Set the count attribute to 0.
        self.image_origin = image  # Set the original image of the bullet.
        self.image = image  # Set the image of the bullet.
        self.rect = self.image.get_rect()  # Get the rectangle of the image.
        self.rect.center = pos  # Set the center of the rectangle to the position.
        self.is_moving = True  # Set the is_moving attribute to True.
        self.direction = direction  # Set the direction of the bullet.
        self.speed = 500  # Set the speed of the bullet to 500.

        # Add physical effects
        self.body = pymunk.Body(1, 1, body_type=pymunk.Body.DYNAMIC)  # Create a body for the bullet.
        self.body.angle = self.direction  # Set the angle of the body to the direction.
        self.body.position = pos  # Set the position of the body to the position.

        # Calculate the x and y speed of the bullet.
        x_speed = self.speed * sin(self.direction / 180 * π)  # Calculate the x speed of the bullet.
        y_speed = self.speed * cos(self.direction / 180 * π)  # Calculate the y speed of the bullet.
        self.body.elasticity = 1.0  # Set the elasticity of the body to 1.0.
        self.body.velocity = (x_speed, y_speed)  # Set the velocity of the body.

        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))  # Create a shape for the bullet.
        self.shape.elasticity = 1.0
        self.shape.collision_type = 3

    def move(self):
        """This method moves the bullet."""
        pass

    def destroy(self):
        """This method destroys the bullet."""
        pass
    
    def rotate(self):
        """This method rotates the bullet."""
        old_center = self.rect.center  # Get the center of the rectangle.
        self.direction %= 360  # Get the direction of the bullet.
        self.image = pygame.transform.rotate(self.image_origin, self.direction)  # Rotate the image of the bullet.
        self.rect = self.image.get_rect()  # Get the rectangle of the image.
        self.rect.center = old_center  # Set the center of the rectangle to the old center.

    def update(self, *args, **kwargs):
        """This method updates the bullet.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        self.rect.center = self.body.position
        self.direction = self.body.angle
        self.rotate()
