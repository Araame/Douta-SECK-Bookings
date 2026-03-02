class Booking:
    def __init__(self, motif, user_id, slot_id, date, event_type):
        self.motif = motif
        self.user_id = user_id
        self.slot_id = slot_id
        self.date = date
        self.event_type = event_type

    
    def __str__(self):
        return f"{self.event_type}| Motif : {self.motif} | {self.date} "