
class TimeKeeper():
    def __init__(self, groups):
        self.groups = groups
    
    def get_groups(self):
        return self.groups
    
    def add_group(self, group):
        self.groups.append(group)
    
    def get_group(self, name):
        for group in self.groups:
            if group.name == name:
                return group
        return None
    
    def delete_group(self, name):
        for group in self.groups:
            if group.name == name:
                self.groups.remove(group)
                return True
        return False
