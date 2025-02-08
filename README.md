# Tank Game

#### Note: This game is still in development. Some features may not function as intended or may fail to execute properly. It is recommended to wait until the project is complete for the best experience.
This project is a simple tank game built using Python and Pygame. The game involves controlling tanks on a map, with the ability to load different tank and map configurations from JSON files.

---

## Table of Contents
- [Requirements](#requirements)
- [Explanation of the files](#explanation-of-the-files)
- [Running the game](#running-the-game)
  - [Setting up the environment](#setting-up-the-environment)
  - [Installing the required dependencies](#installing-the-required-dependencies)
  - [Install Git](#install-git)
  - [Cloning the repository](#cloning-the-repository)
  - [Running the game](#running-the-game-1)
  - [Make a standalone executable (optional)](#make-a-standalone-executable-optional-)
- [Game Rules](#game-rules)
- [Levels of the game](#levels-of-the-game)
- [Inquiry](#inquiry)
- [License](#license)
- [Epilogue](#epilogue)

---

## Requirements

To run this project, you need to have Python 3.8+ installed along with the following dependencies:

- `pygame~=2.6.1`
- `pymunk~=6.9.0`

You can install the required dependencies using the following command:

In Windows:
```sh
pip install -r requirements.txt
```

In macOS/Linux:
```sh
pip3 install -r requirements.txt
```

---

## Explanation of the files:
`background.py` - Contains the `Map` class which is used to draw the background of the game.
`map_test.py` - Contains the test cases for the `Map` class.
`obstacle.py` - Contains the `Obstacle` class which is used to draw the obstacles on the map.
`obstacle_test.py` - Contains the test cases for the `Obstacle` class.
`tank.py` - Contains the `Tank` class which is used to draw the tanks on the map.
`tank_test.py` - Contains the test cases for the `Tank` class.
`config.json` - Contains the configuration for the tanks and the map.
`constants.py` - Contains the constants used in the game.
`level.py` - Contains the `Level` class which is used to load the level from a JSON file.
`LICENSE` - Contains the license information for the project.
`main.py` - Contains the main game loop.
`obstacle.py` - Contains the `Obstacle` class which is used to draw the obstacles on the map.
`README.md` - Contains the README for the project.
`requirements.txt` - Contains the dependencies required for the project.
`tank.py` - Contains the `Tank` class which is used to draw the tanks on the map.

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
```sh
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
```sh
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
```sh
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

### Make a standalone executable (optional)  
You can make a standalone executable by typing the following:  
(In Windows)
```sh
cd C:\path\to\the\repository
pip install pyinstaller
pyinstaller --onefile --windowed --add-data "assets:assets" main.py
```
This will install PyInstaller and create an executable in the `dist` directory.  
Make sure to replace `C:\path\to\the\repository` with the actual path of the repository.

(In macOS/Linux)  
```shell
cd /path/to/the/repository
pip3 install pyinstaller
pyinstaller --onefile --windowed --add-data "assets:assets" main.py
```
This will install PyInstaller and create an executable in the `dist` directory.  
Make sure to replace `/path/to/the/repository` with the actual path of the repository.
---

## Game Rules
1. This is a **2-player** game, thus there are 2 tanks, **red** and **blue** for each player
2. When one tank is defeated by the enemy tank by **colliding with the enemy bullet**, the other player wins. For example, if the **red** tank collides with a bullet from the **blue** tank, then the **blue** tank win.
3. You can shoot bullets using the **space** key for the **blue** tank and the **P** key for the **red** tank.
4. You can move your tank using the **W** key (move forward) or the **S** key (move backward) for the **blue** tank, and the **arrow-up** key (move forward) or the **arrow-down** (move backward) for the **red** tank.
5. You can change the direction of your tank using the **A** key (turn left) or the **D** key (turn right) for the **blue** tank, and the **arrow-left** key (turn left) or the **arrow-right** key (turn right) for the **red** tank.

---

## Levels of the game
There are 4 levels of the game. Each level is harder than the previous one. Here are the levels:   
**Level 1**: This level contains only obstacles on one side.  
**Level 2** (not available yet): This level contains obstacles on both sides.  
**Level 3** (not available yet): Currently not planned, but may be considered in the future.  
**Level 4 (Boss Level)** (not available yet): Currently not planned, but may be considered in the future.

---

## Inquiry
If you have any questions or suggestions, feel free to open an issue or contact me at [here](mailto:pythondeveloper.29042@outlook.com).

---

## License
This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.

---

## Epilogue
Thank you for reading this README. I hope you enjoy playing the game! If you have any questions or suggestions, feel free to contact me or open an issue. Have fun playing the game!

--- 

**THE END**  