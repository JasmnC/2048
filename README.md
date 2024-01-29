
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
   
   - The code is split into several logical parts, follows the flow:
     import modules> set up Pygame environment> initilize variables> main game loop> exception handling
   - The main game loop handles various events, such as mouse clicks, key presses, and window close events.
   - The code includes a try-except block to catch exceptions during execution, ensures that errors are caught and handled gracefully.

</details>

<details>
<summary>User Interface</summary>
   
- The GUI is built with Pygame for displaying the game board, tiles, score, and high score. Ensure that the GUI is intuitive and visually appealing for the players.
- The header bar provides essential information and features, including a welcome message and an information icon for instructions.
- An information panel will appear when the user clicks on the information icon. This feature enhances user experience by providing additional guidance or instructions.
- Game over and restart messages are displayed clearly, ensuring players understand game states.

</details>

<details>
<summary>Error Handling</summary>
   
- The code includes a try-except block to catch exceptions during execution, which helps prevent crashes and ensures a smoother user experience.
- Raises a `ValueError` for invalid key inputs, followed by displaying a warning message to handle unexpected user input.

</details>

### `functions.py`:
<details>
<summary>Functions and Algorithms</summary>
   
- **Tile Movement and Merging**
   - The `take_turn()` function effectively handles tile movement and merging based on the direction provided.
   - Utilizing a matrix approach, the function efficiently shifts tiles and merges them when appropriate, adhering to the rules of the 2048 game.
   - Using boolean matrices to keep track of merged tiles prevents multiple merges of the same tile during a single move.

- **Game Over Detection**:
   - The `check_game_over()` function intelligently checks whether the game is over by examining the board state.
   - It ensures that all cells are filled, and no valid moves (horizontal or vertical) are possible, signaling the end of the game.

- **Random Tile Generation**:
   - The `new_pieces()` function handles the random generation of new tiles upon each turn effectively.
   - It prevents generating new tiles if the board is already full, ensuring the game doesn't become unplayable due to cluttered tiles.
</details>

<details>
<summary>Graphics and Rendering</summary>
   
- **Visual Representation**:
   - The `draw_board()` and `draw_pieces()` functions provide a visually appealing representation of the game board and tiles.
   - Colors are effectively used to differentiate tile values, making it easier for the player to identify and strategize.

- **Information Panel**:
   - The `draw_information()` function creates an information panel when the user clicks on the information icon, offering clear instructions and guidelines.
   - It enhances the user experience by providing necessary information about the game mechanics and controls.

</details>

## Performance:
The code sets the frame rate to 60 frames per second (`fps = 60`), which ensures smooth animation and responsiveness. However, performance may vary depending on the complexity of the game logic and the system's capabilities.

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



