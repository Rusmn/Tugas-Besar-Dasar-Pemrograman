# O.W.C.A. Game 🎮

Embark on an adventure in the world of O.W.C.A.! This project is a text-based adventure game where players can collect monsters, battle in arenas, manage their inventory, and interact with an in-game shop. The game features user registration and login, allowing players to save their progress and compete with others. The core of the game revolves around strategic battles, resource management, and character progression.

## 🚀 Key Features

- **User Authentication:** Secure registration and login system to manage player accounts.
- **Monster Collection:** Collect and manage a variety of unique monsters.
- **Inventory Management:** Keep track of your potions and monsters.
- **Shop System:** Buy and sell items, including monsters and potions.
- **Arena Battles:** Test your skills against randomly generated monsters in the arena.
- **Battle System:** Engage in strategic turn-based battles.
- **Laboratory:** Upgrade your monsters to make them stronger.
- **Admin Interface:** Manage monsters and shop inventory.
- **Data Persistence:** Save and load game data using CSV files.

## 🛠️ Tech Stack

- **Language:** Python 🐍
- **UI:** Custom text-based UI (implemented in `ui.py`)
- **Data Storage:** CSV files (managed by `data.py`)
- **Random Number Generation:** Linear Congruential Generator (LCG)
- **Dependencies:**
    - `argparse` (for command-line argument parsing)
    - `time`
    - `os`

## 📦 Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install any necessary dependencies (if any, specify them here. If not, remove this step):

    ```bash
    # pip install <dependency1> <dependency2>
    # No dependencies to install as of now
    ```

### Running Locally

1.  Navigate to the project directory in your terminal.

2.  Run the `main.py` file, providing the data folder name as a command-line argument:

    ```bash
    python main.py <data_folder_name>
    ```

    Replace `<data_folder_name>` with the name of the folder containing your game data (CSV files).

## 📂 Project Structure

```
O.W.C.A./
├── arena.py        # Implements the arena battle functionality
├── battle.py       # Implements the battle system
├── data.py         # Handles data loading and saving from CSV files
├── inputs.py       # Handles user input, validation, and authentication
├── laboratory.py   # Implements the monster upgrade laboratory
├── main.py         # Main entry point of the game
├── management.py   # Implements the monster management system (admin)
├── shop.py         # Implements the shop management functionality
├── ui.py           # Handles user interface elements and display (not provided in summaries)
├── utility.py      # Provides utility functions for string manipulation
└── data/           # Folder containing CSV data files (example)
    ├── monster.csv
    ├── item.csv
    ├── user.csv
    ├── monster_inven.csv
    ├── stuff.csv
    └── monster_shop.csv
```

## 📸 Screenshots

(Add screenshots of the game here to showcase the UI and gameplay)

## 🤝 Contributing

We welcome contributions to the O.W.C.A. game! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, descriptive messages.
4.  Submit a pull request.

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.
