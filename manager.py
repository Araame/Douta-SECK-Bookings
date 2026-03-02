import csv 
import os
from slot import Slots
import pandas
from event import Event
from booking import Booking
from datetime import datetime
from db import DatabaseManager




class Booking_manager:
    def __init__(self):
        self.db = DatabaseManager()
    
    def create_event_type(self):
        """Create an event's type"""

        event_type = input("Event's type : ")
        event = Event(event_type)
        self.db.insert_event_type(event.event_type)


    def make_booking(self, user):
        """Make a booking"""

        motif = input("Motif : ")
        slots = self.db.select_slots()
        print(slots)
        slot_id = int(input("Slot ID :"))
        events = self.db.select_events_type()
        print(events)
        event_type_id = int(input("Event type : "))
        date = datetime.now().date()
        booking = Booking(motif, user["id_staff"], slot_id, date,event_type_id)
        self.db.insert_booking(booking.user["id"], booking.event_type_id, booking.slot_id, booking.motif, booking.date)
    
    def show_free_slots(self):
        """Show free slots by a given date"""
        try:
            date = input("Date (YY-MM-DD) : ")
            free_slots = self.db.free_slots(date)
            if free_slots :
                for slot in free_slots:
                    print(slot)
            else :
                print("There are no avalaible slots for this day")
        
        except Exception as e:
            print(f"Error : {e}")

    
    def show_user_bookings(self, id):
            """Show bookings that are done by the current user"""

            my_bookings = self.db.select_user_bookings(id)
            if my_bookings :
                for my_booking in my_bookings:
                    print(my_booking)
            else :
                print("No booking")

    def create_slot(self):
        """Create a slot"""

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


    def generate_csv(self):
        """Generate a CSV file"""
        content = self.db.select_all_bookings_with_user()
        fields = ["motif", "firstname", "lastname", "call_number","date"]

        with open(f"planning.csv", "w+", encoding= "utf-8") as file :
            csvwriter = csv.writer(file)
            csvwriter.writerow(fields)
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for row in content:
                writer.writerow(row)
            print("File created")
        

bm = Booking_manager()
bm.generate_csv()
