#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project-description: This is a simple tank war game created using Pygame and Pymunk.
@file-name: level.py
@author: PythonDeveloper29042
@author-email: pythondeveloper.29042@outlook.com
@project: TankWarGame
@github-repo: https://github.com/PythonDeveloper29042/TankWarGame.git
@commit-date: 2025-02-08
@description: This file contains the Level class, which is used to create the levels of the game.
"""

import json
from pygame import image


# class Level:
#     pass


def read_json(path: str) -> list:
    """This function reads a JSON file and returns the data as a dictionary.
    Args:
        path (str): The path of the JSON file.
    Returns:
        list: The data of the JSON file.
    """
    with open(path, "r") as file:
        t = json.loads(file.read())
        map = t["level1"]
    return map


def read_map(path: str) -> list | None:
    """This function reads the map from a JSON file and returns it as a list.
    Args:
        path (str): The path of the JSON file.
    Returns:
        list | None: The map data, or None if an error occurred.
    """
    map = None
    try:
        map = read_json(path)
    except Exception as e:
        print("Failed to read the map data.")
        return None
    return map["map"]


def read_obstacle(path: str) -> list | None:
    """This function reads the obsatcles from a JSON file and returns them as a list.
    Args:
        path (str): The path of the JSON file.
    Returns:
        list | None: The obstacles data, or None if an error occurred.
    """
    data = None
    try:
        data = read_json(path)
    except Exception as e:
        print("Failed to read the obstacles data.")
        return None
    return data["obstacle"]


def read_tank(path: str) -> list | None:
    """This function reads the tank from a JSON file and returns it as a list.
    Args:
        path (str): The path of the JSON file.
    Returns:
        list | None: The tank data, or None if an error occurred.
    """
    data = None
    try:
        data = read_json(path)
    except Exception as e:
        print("Failed to read the tank data.")
        return None
    return data["tank"]


if __name__ == "__main__":
    read_map("assets/config.json")
