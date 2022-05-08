
from Classes.Group import Group
from Classes.TimeEntry import TimeEntry
from Classes.TimeKeeper import TimeKeeper


def deserializeFile(groups):
    tempGroups = []
    if groups is not None:
        for group in groups:
            tempTimeEntries = []
            if len(group['timeEntries']) > 0:
                for temp in group['timeEntries']:
                    timeEntry = TimeEntry(temp['startTime'], temp['endTime'], temp['date'])
                    tempTimeEntries.append(timeEntry)
            newGroup = Group(group['name'], tempTimeEntries)
            tempGroups.append(newGroup)
    return TimeKeeper(tempGroups)