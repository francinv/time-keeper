from CLI.Content import greeting, options
from CLI.GroupMenu import group_menu
from CLI.TimeMenu import time_menu
from CLI.DataMenu import data_menu
from Persistence.Store import loadTimeKeeper

def menu():
    print(greeting)
    input_menu = input(options)
    timeKeeper = loadTimeKeeper()
    handle_input(input_menu, timeKeeper)

def handle_input(input, timeKeeper):
    if input == "1":
        group_menu(timeKeeper)
    elif input == "2":
        time_menu(timeKeeper)
    elif input == "3":
        data_menu(timeKeeper)
    elif input == "4":
        print("Exiting...")
        exit()