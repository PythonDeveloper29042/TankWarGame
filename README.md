# Tank Game

This project is a simple tank game built using Python and Pygame. The game involves controlling tanks on a map, with the ability to load different tank and map configurations from JSON files.

## Requirements

To run this project, you need to have Python installed along with the following dependencies:

- `pygame~=2.6.1`
- `pymunk~=6.9.0`

You can install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Explanation of the files:
`background.py` - Contains the `Map` class which is used to draw the background of the game.
`map_test.py` - Contains the test cases for the `Map` class.
`obstacle.py` - Contains the `Obstacle` class which is used to draw the obstacles on the map.
`obstacle_test.py` - Contains the test cases for the `Obstacle` class.
`tank.py` - Contains the `Tank` class which is used to draw the tanks on the map.
`tank_test.py` - Contains the test cases for the `Tank` class.
`collide.py` - Contains the `Collide` class which is used to check for collisions between the tanks and the obstacles.
`config.json` - Contains the configuration for the tanks and the map.
`constants.py` - Contains the constants used in the game.
`level.py` - Contains the `Level` class which is used to load the level from a JSON file.
`LICENSE` - Contains the license information for the project.
`main.py` - Contains the main game loop.
`obstacle.py` - Contains the `Obstacle` class which is used to draw the obstacles on the map.
`README.md` - Contains the README for the project.
`requirements.txt` - Contains the dependencies required for the project.
`tank.py` - Contains the `Tank` class which is used to draw the tanks on the map.
`weapon.py` - Contains the `Weapon` class which is used to draw the weapons on the map.

---

## Running the game
...

---

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.
