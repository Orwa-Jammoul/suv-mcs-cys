# This script utilizes the pyautogui, keyboard, and pygetwindow libraries to interact with the active window.
# It includes a function to retrieve the title of the active window and a delay time setting.
# Make sure to install the required libraries before running this code:
# - pyautogui: pip install pyautogui
# - keyboard: pip install keyboard
# - pygetwindow: pip install pygetwindow

import pyautogui
import keyboard
import pygetwindow as gw
import itertools
import time
import sys

dTime=.01

def get_active_window_title():
    """
    Retrieves the title of the currently active window.
    Returns:
        str: The title of the active window if it exists, None otherwise.
    """
    active_window = gw.getActiveWindow()
    if active_window is not None:
        return active_window.title


# This function generates combinations of characters of increasing length and checks if it satisfies a condition.
# It iterates over different lengths of combinations and prints the right one.
# If a combination meets the condition defined by the isItRight function, it prints the password and exits.

def create_combinations():
    """
    Generates combinations of characters of increasing length and checks if it satisfies a condition.
    
    Iterates over different lengths of combinations and prints them.
    If a combination meets the condition defined by the isItRight function, it prints the password and exits.
    """
    for i in range(1, 9):
        print(f"Printing combinations of length {i}:")
        combinations = itertools.product(range(32, 128), repeat=i)
        for combination in combinations:
            chars = ''.join(chr(c) for c in combination)
            if(isItRight(chars)):
                print(f"Yeeeeeeeees the password is: ({chars})")
                sys.exit()
        print()


# This function checks if a given character combination is correct based on the active window title.
# It interacts with the active window by simulating key presses and retrieves the window title.
# If the window title is not "Enter password", it writes the characters and checks for errors.
# If an error is encountered, it returns False; otherwise, it returns True.

def isItRight(chars):
    """
    Checks if a given character combination is correct based on the active window title.
    
    Interacts with the active window by simulating key presses and retrieves the window title.
    If the window title is not "Enter password", it writes the characters and checks for errors.
    
    Args:
        chars (str): The character combination to be checked.
    
    Returns:
        bool: True if the character combination is correct, False otherwise.
    """
    print(f"Checking: ({chars})")
    wt = get_active_window_title()
    
    if "Enter password" != wt:
        if "Error" == wt:
            pyautogui.press('enter')
            time.sleep(dTime)
        else:
            return True
    
    pyautogui.write(chars)
    time.sleep(dTime)
    pyautogui.press('enter')
    wt = get_active_window_title()

    while wt=="":
      time.sleep(dTime)
      wt = get_active_window_title()

    if "Error" == wt:
        return False
    else:
        return True

# This script initiates the process of hacking a password by registering a hotkey combination (Ctrl + Shift + A) to start the process.
# It prints a message indicating the hacking process is in progress and calls the create_combinations function.
# The script listens for the hotkey combination to trigger the main function in the background.

def main():
    """
    Initiates the process of hacking a password by printing a progress message and calling create_combinations.
    """
    print("Hacking password in progress..")
    create_combinations()

# Register a hotkey (Ctrl + Shift + A) to trigger the main function
keyboard.add_hotkey('ctrl+shift+a', main)

# Listen for events in the background to detect the hotkey combination
keyboard.wait()

