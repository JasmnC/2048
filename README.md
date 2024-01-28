
# 2048 Clone
### A python game inspired by the popular game [2048](https://play2048.co) and this [tutorial](https://www.youtube.com/watch?v=rp9s1O3iSEQ)

## Introduction

This project focuses on the algorithm of the movement and merging logic for tiles in the 2048 game, and implements pygame libraries for user interface for a better game experiance.
All of the enhancment were done in python. 

## Enhancment overview:
The code has undergone several optimizations and improvements to enhance readability, maintainability, and user experience. The major changes include:

1. **Code Modularization:**
   - The code has been split into two files: `game.py` and `functions.py`.
   - `game.py` contains the main game loop and user interface logic.
   - `functions.py` contains reusable functions responsible for game mechanics.

2. **Invalid Key Handling:**
   - Added exception handling to ensure smooth gameplay.
   - Invalid input is gracefully handled, displaying a message to the user.

3. **Game Logic Refinement:**
   - Improved game logic for checking game over conditions.
   - Tiles and text rendering functions are optimized for better performance.

4. **User Interface Enhancements:**
   - Added a header bar includes a welcome message and an information icon for instructions.
   - Information panel displays game instructions upon user interaction.
   - Redesigned the board display to provide better visual feedback to the player.

## Code Review

### `game.py`:
<details>
<summary>Structure and Flow</summary>

- The code follows a clear structure with a well-defined main game loop.
- Event handling for user input is appropriately structured and easy to follow.
- Exception handling ensures that errors are caught and handled gracefully, maintaining a smooth gameplay experience.

</details>

<details>
<summary>User Interface</summary>

- The user interface is intuitive and well-designed.
- The header bar provides essential information and features, including a welcome message and an information icon for instructions.
- Game over and restart messages are displayed clearly, ensuring players understand game states.

</details>

<details>
<summary>Error Handling</summary>

- Exception handling is implemented effectively to handle invalid inputs and unexpected errors.
- Error messages are displayed to the user, providing feedback on incorrect inputs.

</details>

### `functions.py`:
<details>
<summary>Modularization</summary>

- Code is appropriately modularized with reusable functions for game mechanics.
- Each function is focused on a specific task, enhancing code readability and maintainability.

</details>

<details>
<summary>Game Logic</summary>

- The game logic for tile movement, merging, and game over checking is implemented logically and efficiently.
- Functions such as `take_turn` and `check_game_over` handle game mechanics accurately and effectively.

</details>

<details>
<summary>Graphics and Rendering</summary>

- Tile rendering and board display functions are optimized for performance.
- Colors and fonts are chosen thoughtfully to provide a visually pleasing experience to the player.

</details>

<details>
<summary>Documentation</summary>

- Function names and variable names are descriptive, enhancing code readability.
- Comments could be added to explain complex logic or enhance understanding in certain areas.

</details>

## Usage
To run the 2048 game, follow these steps:

1. **Clone the Repo:**

    ```bash
    git clone https://github.com/JasmnC/2048.git
    ```
    
2. **Navigate to the Directory:**
    ```bash
    cd 2048
    ```
    
3. **Install Dependencies:**
    ```bash
    pip install pygame
    ```

4. **Run the Game:**
   This command executes the main Python file, `game.py`, and starts the 2048 game.
    ```bash
    python game.py
    ```

5. **Interact with the Game:**
    - Use the arrow keys (UP, DOWN, LEFT, RIGHT) to move the tiles in the respective direction.
    - Merge tiles with the same value to achieve higher numbers.
    - The game ends when the board is filled, and no valid moves are possible.
    - Press ENTER to restart the game after it ends.

6. **Enjoy!**
    Have fun playing the 2048 game and aim for the highest score possible!



