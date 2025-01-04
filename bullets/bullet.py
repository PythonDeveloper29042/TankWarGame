
"""
@description: This module contains the Bullet class.
"""
from pygame.surface import Surface  # Import the Surface class from the pygame module.
from pygame.sprite import Sprite  # Import the Sprite class from the pygame module.


# Create the Bullet class.
class Bullet(Sprite):
    def __init__(self, image: Surface, direction: int):
        """
        Initializes the Bullet class.
        Args:
            image (Surface): The image of the bullet.
            direction (int): The direction of the bullet.
        """
        super().__init__()
        self.image = image  # Set the image of the bullet.
        self.rect = self.image.get_rect()  # Get the rectangle of the image.
        self.is_moving = True  # Set the is_moving attribute to True.
        self.direction = 0  # Set the direction of the bullet to 0.
        self.speed = 10  # Set the speed of the bullet to 10

    def move(self):
        """This method moves the bullet."""
        pass

    def destroy(self):
        """This method destroys the bullet."""
        pass

    def update(self, *args, **kwargs):
        """This method updates the bullet.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        pass