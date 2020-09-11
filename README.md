# Read Me

Having dabbled with Python and Pygame a few times, I decided to make a full project in Pygame. This is the result: Connect Four AI v. Player.

The AI is powered by MCTS heuristic algorithm (Monte Carlo Tree Search). I implemented this algorithm solely based on my previous knowledge.

Made in 4 days (\~10 hrs)

Scroll down for:
- Install instructions
- Game instructions

## Preview

![Game](/img/preview_game.png?raw=true "Game")
![Terminal](/img/preview_command_line.png?raw=true "Terminal")

## Prerequisites

Python3 and Pygame must be installed first.

Check python version:
```sh
$ python --version
```

Download Python 3 if you do not have it:
https://www.python.org/downloads/

If you have both Python 2 and Python 3 installed, default to Python 3:
```sh
$ alias python=python3
$ python --version
```

Install Pygame:
```sh
$ python3 -m pip install -U pygame --user
```

Check Pygame is installed by running an example project:
```sh
$ python3 -m pygame.examples.aliens
```

## Install and run

Download this repository via Code -> Download ZIP

Replace FILE_PATH with the file path (you can also drag and drop folder into command line)
```sh
$ cd FILE_PATH
$ python3 main.py
```

## Game instructions

Use keys 1-7 to drop a disc in the respective column. AI starts first. Good luck!



*Freddy Jiang*









