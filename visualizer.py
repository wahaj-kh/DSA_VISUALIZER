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


def binary_search_visual(arr, target):
    """Visualizes Binary Search tracking Low, Mid, and High pointers."""

    sorted_arr = sorted(arr)
    
    low = 0
    high = len(sorted_arr) - 1
    steps = 0
    found = False
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2 
        

        clear_screen()
        print("--- BINARY SEARCH VISUALIZER ---")
        print(f"Searching for target: {target} | Split Step: {steps}\n")
        
        pointer_line = [" "] * len(sorted_arr)
        pointer_line[low] = "L"
        pointer_line[mid] = "M"
        pointer_line[high] = "H"
        

        print("Array:    " + "   ".join(map(str, sorted_arr)))
        print("Markers:  " + "   ".join(pointer_line) + "  (L=Low, M=Mid, H=High)\n")

        time.sleep(3)
        

        if sorted_arr[mid] == target:
            found = True
            print(f"--> Success! Target {target} found at index {mid}!")
            break
        elif sorted_arr[mid] < target:
            print(f"--> {sorted_arr[mid]} is too small! Throwing away the left half.")
            low = mid + 1  
            time.sleep(3)
        else:
            print(f"--> {sorted_arr[mid]} is too big! Throwing away the right half.")
            high = mid - 1  
            time.sleep(3)
            
    if not found:
        print(f"\n--> Target {target} was not found in the array.")
        
    input("\nPress Enter to return to the main menu...")
def main_menu():
    while True:
        clear_screen()
        print("=========================================")
        print("   DSA ALGORITHMIC VISUALIZER SYSTEM     ")
        print("=========================================")
        print("1. Visualize Bubble Sort")
        print("2. Visualize Binary Search")
        print("3. Exit Program")
        print("=========================================")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            sample_data = [5, 1, 4, 2]
            bubble_sort_visual(sample_data)
        elif choice == '2':
            sample_data = [10, 23, 4, 87, 56, 32, 19]
            
            clear_screen()
            print("--- BINARY SEARCH CONFIGURATION ---")
            print(f"Available data pool: {sorted(sample_data)}")
            
            try:
                target_input = int(input("\nEnter an integer number to search for: "))
                binary_search_visual(sample_data, target_input)
            except ValueError:
                print("\n[Error] That wasn't a valid integer number!")
                time.sleep(1.5)
            
        elif choice == '3':
            print("\nExiting. Thank you for using the Visualizer!")
            break
        else:
            print("\n[Error] Invalid choice! Please select 1, 2, or 3.")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()