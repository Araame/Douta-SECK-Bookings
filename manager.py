import csv
import re
from datetime import datetime
from db import DatabaseManager

class Booking_manager:
    def __init__(self):
        self.db = DatabaseManager()

    def _get_valid_input(self, prompt, pattern, error_msg):
        while True:
            user_input = input(prompt).strip()
            if re.match(pattern, user_input):
                return user_input
            print(f"Errorr : {error_msg}")


    def create_event_type(self):
        event_type = self._get_valid_input(
            "Event's type : ", r"^[a-zA-Z\s\-]$","Letters only"
        )
        self.db.insert_event_type(event_type)



    def make_booking(self, user_id):
        motif = self._get_valid_input(
            "Motif : ", r"^.{5,500}$", "Letters only"
        )
        
        self.show_slots()
        slot_id = self._get_valid_input("Slot ID : ", r"^\d+$", "Numbers only")
        
        events = self.db.select_events_type()
        print(events)
        event_type = self._get_valid_input("Event type ID : ", r"^\d+$", "Numbers only")
        
        date = self._get_valid_input(
            "Date (YYYY-MM-DD) : ", r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", "Date must be in  YYYY-MM-DD "
        )

        if datetime.strptime(date, "%Y-%m-%d").date() < datetime.now().date():
            print("Invalid date.")

        self.db.insert_booking(user_id, int(event_type), int(slot_id), motif, date)
        print(f"Booking for {date} saved")

    def show_free_slots(self):
        try:
            date = self._get_valid_input(
                "Date (YYYY-MM-DD) : ", r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", "Format YYYY-MM-DD."
            )
            if datetime.strptime(date, "%Y-%m-%d").date() < datetime.now().date():
                print("Invalid date.")
            else:
                free_slots = self.db.free_slots(date)
                if free_slots:
                    for slot in free_slots:
                        print(f"Slot : {slot["moment"]}")
                else:
                    print("No available slots")
        except Exception as e:
            print(f"Error : {e}")


    def show_user_bookings(self, id):
        my_bookings = self.db.select_user_bookings(id)
        if my_bookings:
            for booking in my_bookings:
                print(f'{booking["id_booking"]}. Motif : {booking["motif"]} | Date : {booking["date"].strftime("%Y-%m-%d %H:%M:%S")}')                    

        else:
            print("No booking")


    def show_slots(self):
        slots = self.db.select_slots()
        if slots:
            for slot in slots:
                print(f"Slot : {slot["moment"]}")
        else:
            print("No slots")

    def show_events(self):
        events = self.db.select_events_type()
        if events:
            for event in events:
                print(f"{event["id_event"]}. {event["type_event"]}")
        else:
            print("No event type")

    def create_slot(self):
        moment = self._get_valid_input("Moment : ", r"^[a-zA-Z\s]+$", "Letters only.")
        time_pattern = r"^([01]\d|2[0-3]):([0-5]\d)$"
        
        start = self._get_valid_input("Start time (HH:MM) : ", time_pattern, "Format HH:MM.")
        end = self._get_valid_input("End time (HH:MM) : ", time_pattern, "Format HH:MM.")

        try:
            if self.db.insert_slot(moment, f"{start}:00", f"{end}:00"):
                print(f"Slot {moment} added!")
        except Exception as e:
            print(f"Error : {e}")

    def cancel_booking(self):
        booking_id = self._get_valid_input("ID : ", r"^\d+$", "Numbers only")
        try:
            self.db.cancel_booking(int(booking_id))
            print(f"Booking {booking_id} cancelled!")
        except Exception as e:
            print(f"Error : {e}")

    def generate_csv(self):
        """Generate a CSV File"""
        content = self.db.select_all_bookings_with_user()
        fields = ["motif", "firstname", "lastname", "call_number", "date"]

        try:
            with open("planning.csv", "w", encoding="utf-8", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                for row in content:
                    writer.writerow(row)
            print("File created")
            return True
        except Exception as e:
            print(f"Error : {e}")


bm = Booking_manager()
bm.generate_csv()