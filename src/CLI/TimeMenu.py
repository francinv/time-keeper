from CLI.Content import time_options
from CLI.GroupMenu import view_groups
from Classes.TimeEntry import TimeEntry
from Persistence.Store import saveTimeKeeper

def time_menu(timeKeeper):
    while (1):
        input_menu = input(time_options)
        if handle_menu(input_menu, timeKeeper) == 0:
            break

def handle_menu(input, timeKeeper):
    if input == "1":
        add_time_entry(timeKeeper)
    elif input == "2":
        view_time_entries(timeKeeper)
    elif input == "3":
        delete_time_entry(timeKeeper)
    elif input == "4":
        return 0

def add_time_entry(timeKeeper):
    print("This is your groups: ")
    view_groups(timeKeeper)
    group_name = input("Which group would you like to add a time entry to? ")
    group = timeKeeper.get_group(group_name)
    if group is None:
        print("Group not found")
        return
    print("Create time entry:")
    start_time = input("Start time (HH:mm): ")
    end_time = input("End time (HH:mm): ")
    date = input("Date (YYYY-MM-DD): ")
    new_time_entry = TimeEntry(start_time, end_time, date)
    group.add_timeEntry(new_time_entry)
    saveTimeKeeper(timeKeeper)

def view_time_entries(timeKeeper):
    print("This is your groups: ")
    view_groups(timeKeeper)
    group_name = input("Which group would you like to view entries? ")
    group = timeKeeper.get_group(group_name)
    if group is None:
        print("Group not found")
        return
    print("This is your time entries: ")
    listOfTimeEntries = group.get_timeEntries()
    for i in range(len(listOfTimeEntries)):
        print(i+1, "| Start time:", listOfTimeEntries[i].get_start_time(), 
        "End time:", listOfTimeEntries[i].get_end_time(), "Date:", listOfTimeEntries[i].get_date())
    
def delete_time_entry(timeKeeper):
    print("This is your groups: ")
    view_groups(timeKeeper)
    group_name = input("Which group would you like to modify time entries? ")
    group = timeKeeper.get_group(group_name)
    if group is None:
        print("Group not found")
        return
    print("This is your time entries: ")
    listOfTimeEntries = group.get_timeEntries()
    for i in range(len(listOfTimeEntries)):
        print(i+1, "| Start time:", listOfTimeEntries[i].get_start_time(), 
        "End time:", listOfTimeEntries[i].get_end_time(), "Date:", listOfTimeEntries[i].get_date())
    time_entry_name = input("Which time entry would you like to delete (number of element)? ")
    time_entry = group.get_timeEntries()[int(time_entry_name)-1]
    group.delete_timeEntry(time_entry)
    saveTimeKeeper(timeKeeper)

