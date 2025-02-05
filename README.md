# Tank Game

This project is a simple tank game built using Python and Pygame. The game involves controlling tanks on a map, with the ability to load different tank and map configurations from JSON files.

## Requirements

To run this project, you need to have Python 3.8+ installed along with the following dependencies:

- `pygame~=2.6.1`
- `pymunk~=6.9.0`

You can install the required dependencies using the following command:

In Windows:
```batch
pip install -r requirements.txt
```

In macOS/Linux:
```sh
pip3 install -r requirements.txt
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
### Setting up the environment
To run the game, you must confirm that these are installed:
- Python 3.8+
- Pygame 2.0.1
- Pymunk 6.9.0
- Git

If not, you can install them using the following commands:  
#### Install Python on Windows (via WinGet)
```batch
winget install --id=Python.Python --source=msstore
```  
#### Install Python on macOS (via Homebrew)
```sh
brew install python
```
Make sure you have Homebrew installed. If not, you can install it on this site: https://brew.sh/  

#### Note: You do not need to install Python on Linux, as it comes pre-installed.

### Installing the required dependencies
We already discussed the installation of the required dependencies in the Requirements section, check [here](#requirements) for more information.

### Install Git
#### Install Git on Windows (via WinGet)
In Windows, you can install Git using the Windows Package Manager. Run the following command in the Command Prompt:
```cmd
winget install --id=Git.Git --source=msstore
```
This will install Git for Windows using the Windows Package Manager.

#### Install Git on macOS 
In macOS, it's best to use the Apple-provided Git, which is part of the Xcode Command Line Tools. You can install it by running the following command:
```sh
xcode-select --install
```
This will install the Xcode Command Line Tools, which includes Git.

#### Install Git on Linux
In Linux, you can install Git using the package manager of your distribution. For example, in Ubuntu, you can install Git by running the following command:
```sh
sudo apt-get install git
```

### Cloning the repository
After you install Python and Git, it's time to clone the repository! You can do this by running the following command:
```sh
git clone 
```

### Running the game
After all of these steps, you're all set! Now it's time to run the game! You can do this by running the following command:  

In Windows:
```batch
cd C:\path\to\the\repository
python main.py
```
Make sure to replace `C:\path\to\the\repository` with the actual path to the repository on your computer.  

In macOS/Linux:
```sh
cd /path/to/the/repository
python3 main.py
```
Make sure to replace `/path/to/the/repository` with the actual path to the repository on your computer.

---

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.
