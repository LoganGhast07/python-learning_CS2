#Unit 3 Excercise 1: Pickle Basis and Project Structure

def practice_3_beginner():
    """
    Beginner: Basic pickle operations and directory creation
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3.1: Pickle & Project Setup")
    print("=" * 50)
    
    
    import pickle
    import os
    # --- Part A: Pickle ---
    # TODO 1: Create a list to pickle
    shopping_list = ["Apples", "Bananas", "Milk", "Bread"]
    # TODO 2: Save with pickle
    with open("shopping.pkl", "wb") as f:
        # TODO: Use pickle.dump
        pickle.dump(shopping_list, f)
    print("Shopping list pickled!")
    # TODO 3: Load with pickle
    with open("shopping.pkl", "rb") as f:
        loaded_list = pickle.load(f)
    print(f"Loaded list: {loaded_list}")
    # TODO 4: Add items and re-save
    loaded_list.append("Eggs")
    loaded_list.append("Cheese")
    with open("shopping.pkl", "wb") as f:
        # TODO: Save updated list
        pickle.dump(loaded_list, f)

    print("Updated list saved")
    # --- Part B: Directory Structure ---
    # TODO 5: Create project directory
    project_name = "my_project"
    if not os.path.exists(project_name):
    # TODO: Create the directory
        os.makedirs(project_name)
    # TODO 6: Create subdirectories
    subdirs = ["src", "docs", "tests", "data"]
    for subdir in subdirs:
        path = os.path.join(project_name, subdir)
        # TODO: Create each subdirectory
    if not os.path.exists(path):
        os.makedirs(path)
    # TODO 7: Create initial files (README.md, main.py in src)
    # TODO 8: List project structure
    print("\nProject structure:")
    # Run the exercise
practice_3_beginner()

print("=" * 50)

#Unit 3 Excersice 2: File Organizer

def practice_3_intermediate():
    """
    Intermediate: Organize files by type
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3.2: File Organizer")
    print("=" * 50)

    import os
    import shutil
    from pathlib import Path

    messy_folder = "messy_files"

    # TODO: Setup — Create messy folder with test files
    test_files = [
        "document.txt", "image.jpg", "photo.png",
        "report.pdf", "script.py", "data.csv",
        "music.mp3", "video.mp4", "archive.zip"
    ]

    # Create messy folder if missing
    if not os.path.exists(messy_folder):
        os.makedirs(messy_folder)

    # Create each file in messy_folder
    for filename in test_files:
        filepath = os.path.join(messy_folder, filename)
        with open(filepath, "w") as f:
            f.write(f"Test file: {filename}")

    # Category mapping
    organized = {
        "documents": [".txt", ".pdf", ".doc"],
        "images": [".jpg", ".png", ".gif"],
        "code": [".py", ".js", ".html"],
        "data": [".csv", ".json", ".xml"],
        "media": [".mp3", ".mp4", ".avi"],
        "archives": [".zip", ".tar", ".rar"]
    }

    # TODO: Create organized folders for each category
    for category in organized.keys():
        category_path = os.path.join(messy_folder, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

    # TODO: Organize files
    for filename in os.listdir(messy_folder):
        file_path = os.path.join(messy_folder, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)

            # Find matching folder
            for category, extensions in organized.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(messy_folder, category)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    break

    # TODO: Show organized structure
    print("\nOrganized structure:")
    for category in organized.keys():
        category_path = os.path.join(messy_folder, category)
        if os.path.exists(category_path):
            print(f"\n{category.capitalize()}:")
            for file in os.listdir(category_path):
                print(f"  - {file}")


# Run the exercise
practice_3_intermediate()


print("=" * 50)

#Unit 3 Excercise 3: Game Save System with backup

import pickle
import os
import shutil
from datetime import datetime
from pathlib import Path

# -------------------------
# FIX: Move GameState here
# -------------------------
class GameState:
    def __init__(self):
        self.player_name = ""
        self.level = 1
        self.score = 0
        self.inventory = []
        self.position = (0, 0)

    def __str__(self):
        return f"{self.player_name} - Level {self.level}, Score: {self.score}"


def practice_3_advanced():
    """
    Advanced: Complex object serialization and backup system
    """
    print("\n" + "=" * 50)
    print("EXERCISE 3.3: Game Save System")
    print("=" * 50)

    # TODO 2: Create and populate a game state
    game = GameState()
    game.player_name = "Hero"
    game.level = 5
    game.score = 1250
    game.inventory = ["Sword", "Shield", "Potion"]
    game.position = (10, 25)

    # TODO 3: Create saves directory and save game with pickle
    saves_dir = "saves"
    if not os.path.exists(saves_dir):
        os.makedirs(saves_dir)

    save_path = os.path.join(saves_dir, "save1.pkl")
    with open(save_path, "wb") as f:
        pickle.dump(game, f)
    print(f"Game saved to {save_path}")

    # TODO 4: Load and verify saved game
    with open(save_path, "rb") as f:
        loaded_game = pickle.load(f)

    print("Loaded game state:")
    print(f"Player Name: {loaded_game.player_name}")
    print(f"Level: {loaded_game.level}")
    print(f"Score: {loaded_game.score}")
    print(f"Inventory: {loaded_game.inventory}")
    print(f"Position: {loaded_game.position}")

    # TODO 5: Implement multiple save slots
    def save_game(game_state, slot_number):
        save_path = os.path.join(saves_dir, f"save{slot_number}.pkl")
        with open(save_path, "wb") as f:
            pickle.dump(game_state, f)
        print(f"Game saved to {save_path}")

    # TODO 6: List all save files
    def list_save_files():
        for file in os.listdir(saves_dir):
            if file.endswith(".pkl"):
                print(f"  - {file}")

    # TODO 7: Create backup function
    def create_backup(source_dir, backup_dir="backups"):
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"backup_{timestamp}")

        shutil.copytree(source_dir, backup_path)
        print(f"Backup created at {backup_path}")

    # TODO 8: Verify backup
    def verify_backup(source, backup):
        source_files = set(os.listdir(source))
        backup_files = set(os.listdir(backup))
        missing_files = source_files - backup_files

        if missing_files:
            print(f"Missing files in backup: {missing_files}")
        else:
            print("Backup verification successful. All files are present.")

    # TODO 9: Cleanup old backups
    def cleanup_old_backups(backup_dir, keep_count=3):
        backups = sorted(
            [os.path.join(backup_dir, d) for d in os.listdir(backup_dir)],
            key=os.path.getmtime,
            reverse=True
        )

        for old_backup in backups[keep_count:]:
            shutil.rmtree(old_backup)
            print(f"Deleted old backup: {old_backup}")

practice_3_advanced()
