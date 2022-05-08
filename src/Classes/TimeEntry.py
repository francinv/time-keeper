import datetime

class TimeEntry:
    def __init__(self, start_time, end_time, date):
        self.start_time = start_time
        self.end_time = end_time
        self.date = date
    
    def get_start_time(self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    def get_date(self):
        return self.date

    def get_duration(self):
        startTime = datetime.datetime.strptime(self.start_time, "%H:%M")
        endTime = datetime.datetime.strptime(self.end_time, "%H:%M")
        time_interval = endTime - startTime
        return time_interval.total_seconds()
    
    def isMonth(self, month):
        dateOfEntry = datetime.datetime.strptime(self.date, "%Y-%m-%d")
        return dateOfEntry.strftime('%B') == month
