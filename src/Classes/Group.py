
class Group:
    def __init__(self, name, timeEntries):
        self.name = name
        self.timeEntries = timeEntries
    
    def get_name(self):
        return self.name
    
    def get_timeEntries(self):
        return self.timeEntries
    
    def add_timeEntry(self, timeEntry):
        self.timeEntries.append(timeEntry)
    
    def delete_timeEntry(self, timeEntry):
        self.timeEntries.remove(timeEntry)
    
    def calculate_total_duration(self, wantedMonth):
        tempTimeEntries = []
        workedSeconds = 0
        for timeEntry in self.get_timeEntries():
            if timeEntry.isMonth(wantedMonth):
                tempTimeEntries.append(timeEntry)
        
        for timeEntry in tempTimeEntries:
            workedSeconds += timeEntry.get_duration()

        return workedSeconds / 3600