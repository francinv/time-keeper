from CLI.Content import group_options, this_is_groups
from Classes.Group import Group
from Persistence.Store import saveTimeKeeper

def group_menu(timeKeeper):
    while (1):
         if handle_input(input(group_options), timeKeeper) == 0:
            break

def handle_input(input, timeKeeper):
    if input == "1":
        add_group(timeKeeper)
    elif input == "2":
        view_groups(timeKeeper)
    elif input == "3":
        delete_group(timeKeeper)
    elif input == "4":
        return 0

def add_group(timeKeeper):
    new_group_name = input("Enter group name: ")
    newGroup = Group(new_group_name, [])
    timeKeeper.add_group(newGroup)
    saveTimeKeeper(timeKeeper)
    print("Group added")

def view_groups(timeKeeper):
    allGroups = timeKeeper.get_groups()
    for group in allGroups:
        print(group.get_name())

def delete_group(timeKeeper):
    print(this_is_groups)
    view_groups(timeKeeper)
    group_name = input("Which group would you like to delete? ")
    if timeKeeper.delete_group(group_name):
        saveTimeKeeper(timeKeeper)
        print("Group deleted")
    else:
        print("Group not found")