import os
import time

def clear_screen():
    """Clears the terminal screen so the visualizer frames don't stack up."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("=========================================")
        print("   DSA ALGORITHMIC VISUALIZER SYSTEM     ")
        print("=========================================")
        print("1. Visualize Bubble Sort (Coming Soon)")
        print("2. Visualize Binary Search (Coming Soon)")
        print("3. Exit Program")
        print("=========================================")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            print("\n[System] Bubble Sort module is under construction...")
            time.sleep(2)  # Holds the text on screen for 2 seconds
        elif choice == '2':
            print("\n[System] Binary Search module is under construction...")
            time.sleep(2)
        elif choice == '3':
            print("\nExiting. Thank you for using the Visualizer!")
            break
        else:
            print("\n[Error] Invalid choice! Please select 1, 2, or 3.")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()