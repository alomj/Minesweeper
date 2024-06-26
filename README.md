# Minesweeper
The game features a grid of clickable squares with hidden "mines" scattered across the board. The goal is to clear the board without detonating any minis by using the number of mines clues next to each square

## Features:
- Classic Minesweeper mechanics: clicking to reveal, flagging suspected mines, and losing when a mine is clicked.
- Visual feedback for game won or lost.
- Simple and intuitive graphical user interface.


## Installation:

To run this project locally, follow these steps:
1. **Clone the repository:**
```bash
git clone https://github.com/alomj/minesweeper.git
```
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pygame.

```bash
pip install pygame
```

## Usage:
To start the game, run the main.py script. This will initialize a Minesweeper board and open a Pygame window where you can play the game.

## Code Structure:
 **main.py:** The entry point of the game. It initializes the game settings and starts the game loop.
 
 **game.py:** Contains the Game class, which handles the game logic, drawing the game board, handling user input, and updating the game state.
 
 **board.py:** Contains the Board class, which represents the Minesweeper board and manages the pieces (cells) on the board.
 
 **piece.py:** Contains the Piece class, which represents an individual cell on the board.

## Screenshots: 
![image](https://github.com/alomj/Minesweeper/assets/144105248/e8632010-2785-4f3a-9a42-61fd567881d8)

![image](https://github.com/alomj/Minesweeper/assets/144105248/131690bd-7d92-459e-898b-0ea513053cc6)

![image](https://github.com/alomj/Minesweeper/assets/144105248/8555e94a-c248-424a-8043-ebc5122332fe)


## Feel free to contribute to the project by opening issues or submitting pull requests.  

**Enjoy playing Minesweeper!**


