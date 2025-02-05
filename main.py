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
import tkinter  # Import the tkinter module for the GUI.
from tkinter import messagebox  # Import the messagebox module from tkinter for the message box.
# from tank.tank import Tank
# from obstacle import Obstacle
# from weapon import Weapon
# from collide import Collide
# from constants import *
from map.background import Map
from obstacle.obstacle import Obstacle
from tank.tank import Tank
from level import *
from bullets.bullet import Bullet
from math import sin, cos, pi as π


class TankMain:
    def __init__(self):
        pygame.init()  # Initialize the pygame module.
        self.load_music()  # Load the music.
        self.winner = None  # Initialize the winner to None.
        self.screen = pygame.display.set_mode((918, 515))  # Set the screen size.
        self.last_camp = 0  # Set the last camp time to 0.
        self.running = True  # Set the running flag to True.
        map_data = read_map("./config.json")  # Read the map data from the config file.
        self.obstacle_data = read_obstacle("./config.json")
        self.tank_data = read_tank("./config.json")
        self.bulletRed_1 = pygame.image.load("./assets/images/Default size/bulletRed1.png").convert_alpha()
        self.bulletBlue_1 = pygame.image.load("./assets/images/Default size/bulletBlue1.png").convert_alpha()
        self.map_obj = Map(
            map_data, self.screen
        )  # Create an instance of the Map class.
        self.obstacle_group = pygame.sprite.Group()  # Create a group for the obstacles.
        self.tank_group = pygame.sprite.Group()  # Create a group for the tanks.
        self.bullet_group = pygame.sprite.Group()  # Create a group for the bullets.

        self.clock = (
            pygame.time.Clock()
        )  # Create a clock object for the game to control the frame rate.

        # Create a space object for the physics engine.
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.create_obstacle()  # Create the obstacles in the game.
        self.create_tank()  # Create the tank in the game.
        self.space.add_collision_handler(3, 2).post_solve = self.collide_bullet_obs_line  # Add a collision handler for the bullet and the obstacle.
        self.space.add_collision_handler(3, 4).post_solve = self.collide_bullet_obs_line  # Add a collision handler for the bullet and the obstacle.
        self.space.add_collision_handler(3, 1).post_solve = self.collide_bullet_tank  # Add a collision handler for the bullet and the tank.
        self.fps = 60  # Set the frame rate of the game.

        # Create the boundaries of the game.
        line_pos = [[(0, 0), (918, 0)], [(918, 0), (918, 515)], [(918, 515), (0, 515)], [(0, 515), (0, 0)]]
        for pos in line_pos:
            line_body = pymunk.Body(10, 10, body_type=pymunk.Body.STATIC)
            line_shape = pymunk.Segment(line_body, pos[0], pos[1], radius=30)
            line_shape.elasticity = 1.0
            self.space.add(line_body, line_shape)

    def load_music(self):
        """This function loads the music in the game."""
        pygame.mixer.init()
        self.bgmusic = pygame.mixer.Sound("./assets/sounds/bgmusic.mp3")
        self.bgmusic.set_volume(0.5)
        self.bgmusic.play(-1)

        self.boom_music = pygame.mixer.Sound("./assets/sounds/boommusic.mp3")
        self.game_scs_music = pygame.mixer.Sound("./assets/sounds/gamesuccess.mp3")
        self.reflect_music = pygame.mixer.Sound("./assets/sounds/reflectmusic.mp3")
        self.shoot_music = pygame.mixer.Sound("./assets/sounds/shootmusic.mp3")
        self.move_music_b1 = pygame.mixer.Sound("./assets/sounds/tankmove.mp3")
        self.move_music_b2 = pygame.mixer.Sound("./assets/sounds/tankmove.mp3")
        self.move_music_r1 = pygame.mixer.Sound("./assets/sounds/tankmove.mp3")
        self.move_music_r2 = pygame.mixer.Sound("./assets/sounds/tankmove.mp3")

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
            "Blue",
            f"./assets/images/Default size/{self.tank_data[0]['image']}.png",
            self.tank_data[0]["pos"],
        )
        self.tank2 = Tank(
            "Red",
            f"./assets/images/Default size/{self.tank_data[1]['image']}.png",
            self.tank_data[1]["pos"],
        )
        self.tank_group.add(self.tank1)
        self.tank_group.add(self.tank2)
        self.space.add(self.tank1.body, self.tank1.shape)
        self.space.add(self.tank2.body, self.tank2.shape)

    def create_bullets(self, type_: str):
        """
        This function creates the bullets in the game.
        Args:
            type_ (str): The type of the bullet.         
        """
        current_time = pygame.time.get_ticks()  # Get the current time of the game.
        if current_time - self.last_camp < 1000:  # If the time difference is greater than 500 milliseconds.
            return
        if len(self.bullet_group) >= 2:
            return
        self.shoot_music.play()
        self.last_camp = current_time  # Set the last camp time to the current time.
        if type_ == 1:
            center_x = self.tank1.rect.centerx  # Get the center x of the tank.
            center_y = self.tank1.rect.centery  # Get the center y of the tank.
            direction = self.tank1.direction  # Get the direction of the tank.
            length = self.tank1.rect.width / 2 + 10  # Get the length of the tank.
            x_length = length * sin(direction / 180 * π)  # Calculate the x length of the tank.
            y_length = length * cos(direction / 180 * π)  # Calculate the y length of the tank.
            pos_x = center_x + x_length  # Calculate the x position of the bullet.
            pos_y = center_y + y_length  # Calculate the y position of the bullet.
            bullet_ = Bullet(self.bulletBlue_1, self.tank1.direction, (pos_x, pos_y))  # Create an instance of the Bullet class.
            self.space.add(bullet_.body, bullet_.shape)  # Add the bullet to the space.
            self.bullet_group.add(bullet_)  # Add the bullet to the bullet group.
        if type_ == 2:
            center_x = self.tank2.rect.centerx  # Get the center x of the tank.
            center_y = self.tank2.rect.centery  # Get the center y of the tank.
            direction = self.tank2.direction  # Get the direction of the tank.
            length = self.tank2.rect.width / 2 + 10  # Get the length of the tank.
            x_length = length * sin(direction / 180 * π)  # Calculate the x length of the tank.
            y_length = length * cos(direction / 180 * π)  # Calculate the y length of the tank.
            pos_x = center_x + x_length  # Calculate the x position of the bullet.
            pos_y = center_y + y_length  # Calculate the y position of the bullet.
            bullet_ = Bullet(self.bulletRed_1, self.tank2.direction, (pos_x, pos_y))  # Create an instance of the Bullet class.
            self.bullet_group.add(bullet_)  # Add the bullet to the bullet group.
            self.space.add(bullet_.body, bullet_.shape)  # Add the bullet to the space.

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
                    self.move_music_b1.play(-1)  #
                    self.tank1.move_forward = True
                if (
                    e.key == K_s
                ):  # If the key pressed is 's', then set the move_backward flag of tank1 to True.
                    self.move_music_b2.play(-1)  #
                    self.tank1.move_backward = True
                if (
                    e.key == K_UP
                ):  # If the key pressed is 'UP', then set the move_forward flag of tank2 to True.
                    self.move_music_r1.play(-1)  #
                    self.tank2.move_forward = True
                if (
                    e.key == K_DOWN
                ):  # If the key pressed is 'DOWN', then set the move_backward flag of tank2 to True.
                    self.move_music_r2.play(-1)  #
                    self.tank2.move_backward = True
                # Shoot bullet event handle
                if e.key == K_SPACE:
                    self.create_bullets(1)
                if e.key == K_p:
                    self.create_bullets(2)

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
                    self.move_music_b1.stop()
                    self.tank1.move_forward = False
                if (
                    e.key == K_s
                ):  # If the key released is 's', then set the move_backward flag of tank1 to False.
                    self.move_music_b2.stop()
                    self.tank1.move_backward = False
                if (
                    e.key == K_UP
                ):  # If the key released is 'UP', then set the move_forward flag of tank2 to False.
                    self.move_music_r1.stop()
                    self.tank2.move_forward = False
                if (
                    e.key == K_DOWN
                ):  # If the key released is 'DOWN', then set the move_backward flag of tank2 to False.
                    self.move_music_r2.stop()
                    self.tank2.move_backward = False

    def collide_bullet_obs_line(self, arbiter: pymunk.Arbiter, space: pymunk.Space, data: dict):
        """This function handles the collision between the bullet and the obstacle.
        Args:
            arbiter (pymunk.Arbiter): The arbiter object.
            space (pymunk.Space): The space object.
            data (dict): The data dictionary.
        """
        self.reflect_music.play()
        bullet, others = arbiter.shapes  # Get the bullet
        for blt in self.bullet_group:  # Loop through the bullet group.
            if blt.shape == bullet:  # If the bullet is found.
                blt.count += 1  # Increment the count of the bullet.
                print(id(blt), blt.count)
                if blt.count >= 5:  # If the count of the bullet is greater than or equal to 5
                    blt.kill()  # Kill the bullet.
                    space.remove(blt.body, blt.shape)  # Remove the bullet from the space.
                break

    def collide_bullet_tank(self, arbiter: pymunk.Arbiter, space: pymunk.Space, data: dict):
        """This function handles the collision between the bullet and the tank.
        Args:
            arbiter (pymunk.Arbiter): The arbiter object.
            space (pymunk.Space): The space object.
            data (dict): The data dictionary.
        """
        bullet, tank = arbiter.shapes
        for blt in self.bullet_group:
            if blt.shape == bullet:
                self.bullet_group.remove(blt)
                self.space.remove(blt.body, blt.shape)
                break
        
        for tnk in self.tank_group:
            if tnk.shape == tank:
                if tnk.name == "Blue":  # If the tank is blue, then set the winner to red.
                    self.winner = "Red"
                if tnk.name == "Red":  # If the tank is red, then set the winner to blue.
                    self.winner = "Blue"
                tnk.kill()
                self.space.remove(tnk.body, tnk.shape)
                self.game_success()
                break

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
            self.bullet_group.draw(self.screen)
            self.bullet_group.update()  # Update the bullets in the game.
            pygame.display.update()

    def game_success(self):
        """This function displays the success message of the game."""
        root = tkinter.Tk()  # Create a tkinter window.
        root.withdraw()  # Hide the tkinter window.
        messagebox.showinfo("Congratulations", f"{self.winner} win!")  # Show the success message.
        root.destroy()  # Destroy the tkinter window.


def main():
    """This is the main function of the game."""
    tank_main = TankMain()  # Create an instance of the TankMain class.
    tank_main.show()  # Call the show method of the TankMain class to display the game.


if __name__ == "__main__":
    main()
