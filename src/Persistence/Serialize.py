
def serializeTimeKeeper(timeKeeper):
    dict = {
        "groups": [

        ]
    }
    for group in timeKeeper.get_groups():
        tempTimeEntries = []
        for timeEntry in group.get_timeEntries():
            tempEntry = {
                "startTime": timeEntry.get_start_time(),
                "endTime": timeEntry.get_end_time(),
                "date": timeEntry.get_date(),
            }
            tempTimeEntries.append(tempEntry)
        groupDict = {
            "name": group.get_name(),
            "timeEntries": tempTimeEntries
        }
        dict["groups"].append(groupDict)
    return dict