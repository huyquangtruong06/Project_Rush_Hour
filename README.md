# 🚗 RUSH HOUR PUZZLE - COURSE PROJECT

## 1️⃣ GENERAL INFORMATION

- **📌 Project name**: Simulate the game Rush Hour and solve the traffic jam problem using a search algorithm  
- **🐍 Language**: Python 3.x  
- **📚 Library used**: `pygame`  
- **👨‍💻 Author**: Group 20  
- **🎯 Objective**:
  - Display the graphical interface of the game Rush Hour  
  - Draw cars, grids, and exit points on the `pygame` window  
  - Allow zooming, panning, and viewing the status of the cars  
  - Aim to integrate path-finding algorithms in the future  

## 2️⃣ FILE STRUCTURE

- `Main.py`: 🟢 Run the main program  
- `Map.py`: 🗺️ Manage map display and handle mouse/key interactions  
- `Vehicles.py`: 🚙 Define the `Vehicle` class, vehicle type, direction of movement, and vehicle drawing function  
- `define.py`: ⚙️ Contains constants such as colors, cell size, grid size, etc.  
- `RUSHHOUR.png`: 🖼️ Game window icon (optional)  
- `README.md`: 📄 Instruction manual (this file)  

## 3️⃣ INSTRUCTIONS FOR RUNNING THE PROGRAM

1. ✅ Install Python >= 3.10 (preferably 3.11 or later)  
2. ✅ Install `pygame`:
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

  - + / -: Zoom in/out using keyboard

- 📌 Vehicle ID will be displayed in the center of each vehicle (if the box is large enough)
## 5️⃣ SUGGESTIONS FOR FURTHER DEVELOPMENT
- 🖱️ Allow players to select and move vehicles with the mouse
- 🎞️ Display each step of the solution path on the screen
- 📂 Allow reading input status from file
## 6️⃣ COPYRIGHT
- 🆓 Freely share, edit, and study for educational purposes.
