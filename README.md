# Net-Walk

Net-Walk is a Python puzzle prototype inspired by the classic **Net** puzzle from [Simon Tatham's Portable Puzzle Collection](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/).  
It uses **PyGame** to render a grid where the player highlights paths to complete a connected network.

## Features

- **Procedural level generation** (`level_generator.py`)  
  - Builds an odd-sized grid with a central starting node  
  - Randomly assigns connections using up/down/left/right directions  
- **Walking mechanics** (`main.py`)  
  - Tracks lit tiles and player movement  
  - Uses mouse/keyboard input via PyGame  
- **Expandable design**: easy to tweak grid size, add new rules, or visuals

## Requirements

- Python 3.8+
- [pygame](https://pypi.org/project/pygame/)

Install dependencies:
```
pip install pygame
```

## Project Structure
```
Net-Walk/
├── main.py             # Game loop: grid rendering, input, lit path tracking
├── level_generator.py  # Level class: builds grid, manages random connections
├── README.md
└── .gitignore
```

## How It Works

- The Level class creates a square grid (default 5×5) with a central origin (`'c'`).
- Each cell may hold directional links (e.g. `'u'`, `'d'`, `'l'`, `'r'`) with opposite mappings for connectivity.
- The Game class (in `main.py`) loads a new Level, tracks the origin, and updates lit tiles as you play.
- PyGame is used for rendering the grid and handling player input.

## Future Work

- Add scoring or win/loss conditions when all tiles are connected
- Better visuals (sprites, colors, highlighting)
- Menu system and restart option

## Acknowledgment

This project is directly inspired by the [Net puzzle in Simon Tatham's Portable Puzzle Collection](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/net.html).
