from db import DatabaseManager



class Slots:
    def __init__(self, moment, start, end):
        self.moment = moment
        self.start = start
        self.end = end
        self.db = DatabaseManager()

    
    def __str__(self):
        return f"{self.moment}| From {self.start} To {self.end}|"
    
    def create_slot(self):
        try:
            moment = input("Moment : ")
            start = input("Start time (HH : MM) : ")
            start_hours, start_minutes = start.split(":")
            end = input("End time : ")
            end_hours, end_minutes = end.split(":")
            slot = Slots(moment, start, end)
            if self.db.insert_slot(slot.moment, slot.time(int(start_hours), int(start_minutes), 00), slot.time(int(end_hours), int(end_minutes), 00)):
                print(f"Slot {moment} added! ")
        except ValueError:
            print("Error")
