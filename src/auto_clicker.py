from pynput.mouse import Controller as mController, Listener, Button
from pynput.keyboard import Controller as kbController, Listener, Key
from time import sleep
import os
import json

mouse = mController()
kb = kbController()

click_count = 0
clicking = False
click_interval = 0 # Seconds
click_limit = 50

def settings():
    global click_count
    global clicking
    global click_interval
    global click_limit

    os.system("cls")

    print("Settings")
    print("======================\n")
    print("1. Clicking Limit")
    print("2. Time inbetween clicks")
    print("3. Exit")

    settings_input = input("\nChoose an option: ")
    if (settings_input == "1"):
        with open("./data/config.json", 'r') as f:
            settings_file = json.load(f)
        print(f"Current limit: {settings_file['click_limit']}")
        click_limit = input("Input new limit: ")


        settings_file["click_limit"] = float(click_limit)

        with open("./data/config.json", 'w') as f:
            json.dump(settings_file, f, indent=4)

        settings()

    elif (settings_input == "2"):
        with open("./data/config.json", 'r') as f:
            settings_file = json.load(f)
        print(f"Current interval in seconds: {settings_file['click_interval']}")
        click_interval = input("Input new interval (Example: 2.4): ")


        settings_file["click_interval"] = float(click_interval)

        with open("./data/config.json", 'w') as f:
            json.dump(settings_file, f, indent=4)

        settings()

    elif (settings_input == "3"):
        exit()

    else:
        settings()

def main_menu():
    global click_count
    global clicking
    global click_interval
    global click_limit

    os.system("cls")

    print("Auto Clicker")
    print("======================\n")
    print("1. Start\n2. Settings\n3. Exit")

    main_input = input("\nChoose an option: ")
    if main_input == "1":
        os.system("cls")

        print("Starting in 5...")
        sleep(1)
        print("Starting in 4...")
        sleep(1)
        print("Starting in 3...")
        sleep(1)
        print("Starting in 2...")
        sleep(1)

        clicking = True
        print("Clicking... (Press R-SHIFT to stop)")
        
    elif main_input == "2":
        settings()
    elif main_input == "3":
        exit()

    else:
        main_menu()

def on_press(key):
    global click_count
    global clicking
    global click_interval
    global click_limit

    try:
        if key == Key.shift_r:
            print("Stop key was pressed")

            clicking = False
            print("Stopped clicking")
            print("Total times clicked: {0}".format(click_count))

            exit()
        else:
            pass

    except AttributeError:
        pass

main_menu()

while clicking == True:
    with open("./data/config.json", 'r') as f:
        settings_file = json.load(f)

    mouse.click(Button.left)
    click_count = click_count + 1
    print("Clicked")
    sleep(settings_file["click_interval"])


    if (click_count == settings_file["click_limit"]):
        clicking = False

        main_menu()

    Listener(on_press = on_press).start()
