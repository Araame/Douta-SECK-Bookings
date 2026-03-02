class Event:
    def __init__(self, event_type):
        self.event_type = event_type

    
    def __str__(self):
        return f"|{self.event_type}"