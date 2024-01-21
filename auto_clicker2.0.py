# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 11:53:20 2024

"""

import time
import os
import subprocess
import sys
import pyautogui

def install_module(module_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
    except Exception as e:
        print(f"Error: {e}")

def check_and_install_modules():
    required_modules = ['pyautogui', 'pyscreeze', 'opencv-python']

    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            print(f"{module} module is missing. Installing...")
            install_module(module)

def is_image_file(file_path):
    image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff']
    _, extension = os.path.splitext(file_path)
    return extension.lower() in image_extensions

def get_desktop_path():
    return os.path.join(os.path.expanduser("~"), "Desktop")

def autoclicker():
    count = 0
    location_given = False

    print("                _         _____ _ _      _             _____  _   _  _____ ")
    print("     /\\        | |       / ____| (_)    | |           |  __ \| \\ | |/ ____|")
    print("    /  \\  _   _| |_ ___ | |    | |_  ___| | _____ _ __| |__) |  \\| | |  __ ")
    print("   / /\\ \\| | | | __/ _ \\| |    | | |/ __| |/ / _ \\ '__|  ___/| . ` | | |_ |")
    print("  / ____ \\ |_| | || (_) | |____| | | (__|   <  __/ |  | |    | |\\  | |__| |")
    print(" /_/    \\_\\__,_|\\__\\___/ \\_____|_|_|\\___|_|\\_\\___|_|  |_|    |_| \\_|\\_____|")
    print("                                                      -Created by lilhaerden")
    print("")
    print("")
    print("")
    print("Program Started..")
    
    check_and_install_modules()

    while True:
        try:
            if not location_given:
                print("")
                file_name = input("Please enter the name of the file on the desktop with its extension (e.g., file.png, file.jpg, or file.jpeg).\n")
                location_given = True
                
            desktop_path = get_desktop_path()

            
            base_name, extension = os.path.splitext(file_name)
            file_path = os.path.join(desktop_path, file_name)

            if not os.path.exists(file_path) or not is_image_file(file_path):
                print(f"Error: '{file_name}' is not a valid image file on the desktop. Please provide a valid image file name.")
                print("")
                location_given = False
                continue

            count += 1
            locateOnScreen = pyautogui.locateOnScreen(file_path, confidence=0.8)

            if locateOnScreen is not None:
                x, y = pyautogui.center(locateOnScreen)
                print("Clicked on the specified image!")
                pyautogui.click(x, y)
                pyautogui.moveTo(x, y + 250)

                choice = input("Image found! Press '1' to continue, '2' to exit: ")
                if choice == '1':
                    count = 0
                elif choice == '2':
                    print("Exiting the program.")
                    return
            else:
                print("Image not found. Continuing...")

        except pyautogui.ImageNotFoundException:
            print("Attempt {}: Image not found. Continuing...".format(count))
            
        time.sleep(5.0)

if __name__ == "__main__":
    autoclicker()
