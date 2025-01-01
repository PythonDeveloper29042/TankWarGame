"""
@description: This module contains the Bullet class.
"""
from pygame.surface import Surface  # Import the Surface class from the pygame module.
from pygame.sprite import Sprite  # Import the Sprite class from the pygame module.


# Create the Bullet class.
class Bullet(Sprite):
    def __init__(self, image: Surface):
        """
        Initializes the Bullet class.
        Args:
            image (Surface): The image of the bullet.
        """
        super().__init__()