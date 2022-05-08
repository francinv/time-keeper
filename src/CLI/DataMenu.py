import datetime
import pandas as pd
import openpyxl
from pathlib import Path
from CLI.Content import data_options
from CLI.GroupMenu import view_groups
from Classes.TimeKeeper import TimeKeeper

def data_menu(timeKeeper):
    while (1):
        if handle_input(input(data_options), timeKeeper) == 0:
            break

def handle_input(input, timeKeeper):
    if input == "1":
        get_time_for_month(timeKeeper)
    elif input == "2":
        export_data_for_month(timeKeeper)
    elif input == "3":
        export_all_data(timeKeeper)
    elif input == "4":
        return 0

def get_time_for_month(timeKeeper):
    print("This is your groups: ")
    view_groups(timeKeeper)
    group_name = input("Which group would you like to get worked hours for? ")
    group = timeKeeper.get_group(group_name)
    month = input("Enter the month you want to get the time for (leave empty if you want for this month): ")
    if month == "":
        month = datetime.datetime.now().strftime('%B')
    else:
        month = month.capitalize()
    if (group is not None):
        print("You worked for " + str(group.calculate_total_duration(month)) + " hours in " + month)

def export_data_for_month(timeKeeper):
    print("This is your groups: ")
    view_groups(timeKeeper)
    group_name = input("Which group would you like to export data for? ")
    group = timeKeeper.get_group(group_name)
    month = input("Enter the month you want to export data for (leave empty if you want for this month): ")
    if month == "":
        month = datetime.datetime.now().strftime('%B')
    else:
        month = month.capitalize()
    if (group is not None):
        fileName = group_name + "_" + month + ".xlsx"
        path = Path.home() / "TimeKeeper" / fileName
        build_export_dataframe(group, month).to_excel(path)
        print("Data exported to " + str(path))

def export_all_data(timeKeeper):
    print("This is your groups: ")
    view_groups(timeKeeper)
    group_name = input("Which group would you like to export data for? ")
    group = timeKeeper.get_group(group_name)
    if (group is not None):
        dataframe = pd.DataFrame(columns=['Group', 'Date', 'Start', 'End', 'Duration'])
        for timeEntries in group.get_timeEntries():
            dataframe.loc[len(dataframe)] = [
                group.get_name(),
                timeEntries.get_date(),
                timeEntries.get_start_time(),
                timeEntries.get_end_time(),
                timeEntries.get_duration() / 3600
            ]
        fileName = group_name + "_all.xlsx"
        path = Path.home() / "TimeKeeper" / fileName
        dataframe.to_excel(path)
        print("Data exported to " + str(path))


def build_export_dataframe(group, month):
    dataframe = pd.DataFrame(columns=['Group', 'Date', 'Start', 'End', 'Duration'])
    exportTimeGroups = []
    for timeEntries in group.get_timeEntries():
        if timeEntries.isMonth(month):
            exportTimeGroups.append(timeEntries)

    for timeEntries in exportTimeGroups:
        dataframe.loc[len(dataframe)] = [
            group.get_name(), 
            timeEntries.get_date(), 
            timeEntries.get_start_time(), 
            timeEntries.get_end_time(), 
            timeEntries.get_duration() / 3600]
    return dataframe
