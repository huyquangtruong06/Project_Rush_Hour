# 🚗 RUSH HOUR PUZZLE - COURSE PROJECT

## 1️⃣ GENERAL INFORMATION

- **📌 Project name**: Simulate the game Rush Hour and solve the traffic jam problem using a search algorithm  
- **🐍 Language**: Python 3.x  
- **📚 Library used**: `pygame`, `copy`, `tracemalloc`, `time`, `deque`, 
- **👨‍💻 Author**: Group 20  
- **🎯 Objective**:
  - Display the graphical interface of the game Rush Hour  
  - Draw cars, grids, and exit points on the `pygame` window  
  - Allow zooming, panning, and viewing the status of the cars  
  - Aim to integrate path-finding algorithms in the future  

## 2️⃣ FILE STRUCTURE
📂 Core Game Files
- `Main.py`: 🟢 Run the main program  
- `Map.py`: 🗺️ Manage map display and handle mouse/key interactions  
- `Vehicles.py`: 🚙 Define the `Vehicle` class, vehicle type, direction of movement, and vehicle drawing function

🔍 Algorithm Implementations
- `A_Algorithm.py`: 🔍 Implements A search with heuristic optimization for Rush Hour solution
- `UCS_Algorithm.py`: ⚖️ Performs UCS algorithm tracking path costs to solve Rush Hour puzzles efficiently
- `BFS_Algorithm.py`: 🌊 Breadth-first search implementation for Rush Hour puzzle solving with performance metrics.
- `DFS_Algorithm.py`: 🌀 Implements DFS with backtracking to solve Rush Hour, tracking performance metrics and visited states.
- `BinaryMinHeap.py`: 📊 Support A_Algorithm.py

🎮 User Interface
- `Button.py`: 🛎️ Creates interactive UI buttons with hover/click detection and responsive positioning.
- `Event.py`: 🎮 Handles all game events including mouse/keyboard inputs, zooming, navigation and auto-play controls
- `KeyboardOperation.py`: 🎛️ Manages algorithm navigation controls including step-by-step movement and auto-play functionality.
- `Menu.py`: 🍔 Displays interactive algorithm selection menu, and with button BACK to back state before.
- `Support.py`: 🛠️ Handles game menus including level selection and start/quit screens with responsive UI elements.

⚙️ Configuration
- `Levels.py`: 📋 List car for ten levels. 
- `Window.py`: 🖥️ Display screen
- `define.py`: ⚙️ Contains constants such as colors, cell size, grid size, etc.  
- `RUSHHOUR.png`: 🖼️ Game window icon (optional)  
- `README.md`: 📄 Instruction manual (this file) 

🖼️ Assets
- `background`: 🎨 Contain images about background
- `button`: 🖼️ Contain images about button
- `music`:  🎵 Contain sounds effect

## 3️⃣ INSTRUCTIONS FOR RUNNING THE PROGRAM
1. ✅ Install Python >= 3.10 (preferably 3.11 or later)  
2. ✅ Install `pygame` and necessary libraries:
   ```bash
   pip install pygame
3. ▶️ Run the program:
   ```bash
   python Main.py
## 4️⃣ USER MANUAL
- 🖱️ Mouse Controls:
  - Middle mouse (scroll):

  - 🔍 Scroll up: Zoom in

  - 🔎 Scroll down: Zoom out

  - Left mouse (click & drag): 🧭 Move/pan the map

  - ⌨️ Keyboard Controls:
  - R: 🔄 Reset view (zoom to original size)
  - I: 🛠️ Inital state
  - Space : 🛠️ To auto play
  - + / -: Zoom in/out using keyboard

## 5️⃣ SUGGESTIONS FOR FURTHER DEVELOPMENT
- 🖱️ Allow players to select and move vehicles with the mouse

- 📂 Allow reading input status from file

## 6️⃣ COPYRIGHT
- 🆓 Freely share, edit, and study for educational purposes.
