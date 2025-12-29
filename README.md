# 🎮 Brick Breaker Game

A classic Breakout-style arcade game built with Python and Pygame. Break all the bricks using your paddle to bounce the ball while avoiding letting it fall off the screen!

## ✨ Features

- **Two Difficulty Modes**
  - **Easy Mode**: 6x6 grid with 3 strength levels
  - **Hard Mode**: 13x6 grid with 6 strength levels and randomized brick strengths
  
- **Game Mechanics**
  - Smooth paddle movement with arrow keys
  - Realistic ball physics and collision detection
  - Multi-hit bricks with visual strength indicators (color-coded)
  - Score tracking system
  - Win/lose conditions
  
- **User Interface**
  - Main menu system
  - Pause menu with options
  - Game over screen with score display
  - Visual feedback for brick destruction

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- Pygame library

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Afreen4115/Brick-Breaker-Game.git
cd Brick-Breaker-Game
```

2. Install Pygame:
```bash
pip install pygame
```

3. Ensure all image assets are in the `images/` directory:
   - `button_audio.png`
   - `button_back.png`
   - `button_keys.png`
   - `button_options.png`
   - `button_quit.png`
   - `button_resume.png`
   - `button_video.png`
   - `hard.png`
   - `soft.png`

## 🎯 How to Play

1. Run the game:
```bash
python breakout.py
```

2. **Controls:**
   - `LEFT ARROW` / `RIGHT ARROW`: Move paddle left/right
   - `SPACE`: Pause game / Access menu
   - `ANY KEY`: Start game / Restart after game over

3. **Objective:**
   - Use the paddle to bounce the ball and break all bricks
   - Each brick requires multiple hits (indicated by color)
   - Don't let the ball fall off the bottom of the screen
   - Clear all bricks to win!

4. **Scoring:**
   - Each brick destroyed awards 100 points
   - Score is displayed when you lose

## 📁 Project Structure

```
Brick-Breaker-Game/
├── main.py              # Main menu implementation
├── breakout.py          # Core game logic (easy & hard modes)
├── button.py            # Button class for UI elements
├── images/              # Game assets (buttons, icons)
│   ├── button_*.png
│   ├── hard.png
│   └── soft.png
└── README.md           # This file
```

## 🛠️ Technologies Used

- **Python 3.x**: Programming language
- **Pygame**: Game development library for graphics and input handling

## 🎨 Game Features Explained

### Brick Strength System
- Bricks have different strength levels (1-6 in hard mode, 1-3 in easy mode)
- Each hit reduces the brick's strength by 1
- Colors indicate strength level:
  - **Easy Mode**: Red (1), Green (2), Blue (3)
  - **Hard Mode**: Red (1), Green (2), Blue (3), Yellow (4), Magenta (5), Peach (6)

### Collision Detection
- Precise collision detection with threshold-based hit detection
- Ball bounces off walls, bricks, and paddle
- Paddle direction affects ball trajectory

### Game States
- **Main Menu**: Initial screen with game options
- **Paused**: Access to settings and resume
- **Playing**: Active gameplay
- **Game Over**: Win/lose screen with restart option

## 🔧 Configuration

You can modify game settings in `breakout.py`:

- **Screen dimensions**: `screen_width` and `screen_height`
- **Grid size**: `cols` and `rows` variables
- **Ball speed**: `speed_x`, `speed_y`, `speed_max` in `game_ball` class
- **Paddle speed**: `speed` in `paddle` class
- **FPS**: `fps` variable (default: 60)

## 🐛 Known Issues

- Image paths in `main.py` are hardcoded for Windows. Update paths for cross-platform compatibility.
- Score reset functionality may need refinement in some game states.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.


---

**Enjoy the game!** 🎮

