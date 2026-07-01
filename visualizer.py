import os
import time

def clear_screen():
    """Clears the terminal screen so the visualizer frames don't stack up."""
    os.system('cls' if os.name == 'nt' else 'clear')


def bubble_sort_visual(arr):
    """Sorts a list of numbers and visualizes it step-by-step."""
    n = len(arr)
    
    temp_list = arr.copy()
    
    for i in range(n):

        for j in range(0, n - i - 1):
            
            # Wipes the screen so the next print looks like an animation frame
            clear_screen()
            print("--- BUBBLE SORT VISUALIZER ---")
            print(f"Comparing pair: {temp_list[j]} and {temp_list[j+1]}")
            print(f"Current Array:  {temp_list}\n")
            
            time.sleep(3)
        
            if temp_list[j] > temp_list[j + 1]:
                print(f"--> {temp_list[j]} > {temp_list[j+1]}! SWAPPING them.")
                
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
                time.sleep(3)
            else:
                print(f"--> {temp_list[j]} is smaller. No swap needed.")
                time.sleep(3)

    clear_screen()
    print("=========================================")
    print("         SORTING COMPLETE!               ")
    print("=========================================")
    print(f"Final Sorted Array: {temp_list}")
    input("\nPress Enter to return to the main menu...")
def main_menu():
    while True:
        clear_screen()
        print("=========================================")
        print("   DSA ALGORITHMIC VISUALIZER SYSTEM     ")
        print("=========================================")
        print("1. Visualize Bubble Sort")
        print("2. Visualize Binary Search (Coming Soon)")
        print("3. Exit Program")
        print("=========================================")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            sample_data = [5, 1, 4, 2]
            bubble_sort_visual(sample_data)
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