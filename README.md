# Asteroids Game

A classic Asteroids arcade game implementation built with Python and Pygame. Navigate through space, destroy asteroids, and avoid collisions in this retro-style space shooter.

## 🎮 Features

- **Classic Gameplay**: Navigate your ship through an asteroid field
- **Smooth Controls**: Rotate and move your ship with responsive controls
- **Shooting Mechanics**: Fire bullets to destroy asteroids
- **Asteroid Splitting**: Large asteroids split into smaller pieces when destroyed
- **Sound Effects**: Immersive audio with shooting sounds, explosions, and player death effects
- **Background Music**: Atmospheric background music for enhanced gameplay experience
- **Visual Design**: Clean white graphics on a space background

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd asteroids
```

2. Install dependencies using uv:
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

### Running the Game

```bash
python main.py
```

Or with uv:
```bash
uv run main.py
```

## 🎯 Controls

- **Arrow Keys** or **WASD**: Rotate and move your ship
- **Space**: Shoot bullets
- **ESC** or **Close Window**: Quit the game

## 📁 Project Structure

```
asteroids/
├── main.py              # Main game loop and initialization
├── player.py            # Player ship logic and controls
├── asteroid.py          # Asteroid behavior and splitting
├── asteroidfield.py     # Asteroid field management
├── bullet.py            # Bullet physics and rendering
├── circleshape.py       # Base circle shape class
├── constants.py         # Game configuration constants
├── logger.py            # Game state logging utilities
├── assets/
│   ├── audio/           # Sound effects and background music
│   └── img/             # Background images
└── pyproject.toml       # Project dependencies and metadata
```

## 🛠️ Technology Stack

- **Python 3.10+**: Core programming language
- **Pygame 2.6.1**: Game development framework
- **uv**: Modern Python package manager

## 🎨 Game Mechanics

- **Player Movement**: Ship moves forward/backward and rotates smoothly
- **Asteroid Spawning**: Asteroids spawn continuously at a configurable rate
- **Collision Detection**: Circular collision detection for player, asteroids, and bullets
- **Asteroid Splitting**: When destroyed, large asteroids split into smaller pieces with randomized velocities
- **Game Over**: Collision with an asteroid ends the game

## 🔮 Future Improvements

- [ ] Add a scoring system
- [ ] Add a menu system
- [ ] Implement multiple lives and re-spawning
- [ ] Add an explosion effect for the asteroids
- [ ] Add acceleration to the player movement
- [ ] Make the objects wrap around the screen instead of disappearing
- [ ] Create different weapon types
- [ ] Make the asteroids lumpy instead of perfectly round
- [ ] Make the ship have a triangular hit box instead of a circular one
- [ ] Add a shield power-up
- [ ] Add a speed power-up
- [ ] Add bombs that can be dropped

## 📝 License

This project is part of a learning exercise. Feel free to use and modify as needed.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Enjoy the game!** 🚀
