import os
import bcrypt
import mysql.connector
from dotenv import load_dotenv
from datetime import datetime



load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.connector = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_DATABASE"),
            auth_plugin='mysql_native_password'
            )
        self.cursor = self.connector.cursor(dictionary=True)

    def commit(self):
        self.connector.commit()
        self.cursor.close()


#Users
    def insert_user(self, firstname, lastname, email, call_number, password):
        """INSERT A USER INTO USERS"""
        self.cursor.execute(
            """INSERT INTO Users(firstname, lastname, email, call_number, password) VALUES (%s, %s, %s, %s, %s)""", (firstname, lastname, email, call_number, password))
        self.commit()
        return True

    
    def verify_credentials(self, email, password):
        """VERIFY IF A USER IS IN THE DB"""
        self.cursor.execute(
            """SELECT * FROM Users WHERE email = %s""", (email,))
        row = self.cursor.fetchone()
        if bcrypt.checkpw(password.encode("utf-8"), row["password"].encode("utf-8")):
            return row 
        else :
            print("Not found")

#Events
    def insert_event_type(self, event):
        """Inserting a new event type"""
        self.cursor.execute(
            """INSERT INTO Events(type_event) values (%s)""", (event,))
        self.commit()

    def select_events_type(self):
        """SELECT EVENTS TYPE"""
        self.cursor.execute(
            """SELECT * FROM Events""")
        return self.cursor.fetchall()

#BOOKINGS
    def insert_booking(self, user_id, event_type, slot_id, motif, date_str):
        """Inserting a new booking"""
        try:
            bookings = self.select_all_date_already_book()
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            current_date = datetime.now().date()
            if current_date > date:
                print("Invalid date")
            

            already_booked = False
            for book in bookings:
                if book["date"] == date and book["slot"] == slot_id:
                    already_booked = True
                    break 

            if already_booked:
                print("Already booked!")
            else:
                self.cursor.execute(
                    """INSERT INTO Bookings(user, event, slot, motif, date) 
                    VALUES (%s, %s, %s, %s, %s)""", 
                    (user_id, event_type, slot_id, motif, date)
                )
                self.commit()
                print("OK")
                            
        except Exception as e :
            print({e})

    def select_user_bookings(self, user_id):
        """SELECT SPECIFIC BOOKINGS OF A USER"""
        self.cursor.execute(
            """SELECT * FROM Bookings WHERE user = %s and confirmed = %s""", (user_id,1))
        return self.cursor.fetchall()
    

    def select_all_bookings(self):
        """SELECT SPECIFIC BOOKINGS OF A USER"""
        self.cursor.execute(
            """SELECT * FROM Bookings where confirmed = %s""", (1,))
        return self.cursor.fetchall()
    

    def select_all_date_already_book(self):
        """SELECT ALL DATES ALREADY BOOK OF A USER"""
        self.cursor.execute(
            """SELECT date, slot FROM Bookings """)
        return self.cursor.fetchall()
    

    def select_all_bookings_with_user(self):
        """SELECT ALL BOOKINGS WITH THEIR USERS"""
        self.cursor.execute(
            """SELECT b.motif, u.firstname, u.lastname, u.call_number, b.date  FROM Bookings b JOIN Users u ON u.id_staff = b.user WHERE id_booking = %s""", (0,))
        return self.cursor.fetchall()
    
    def cancel_booking(self):
        """CANCEL A SPECIFIC BOOKING"""
        id = int(input("ID : "))
        self.cursor.execute("""SELECT confirmed WHERE id_booking = %s""", (0,))
        row = self.cursor.fetchone()
        if row and row == 1:
            self.cursor.execute(
            """UPDATE Bookings SET confirmed = %s WHERE id_booking = %s""", (0, id))
            print("Cancelled")
        print("Cancelled booking")

        return True
    

#SLOTS
    def insert_slot(self, moment, start, end):
        """Inserting a new slot"""
        self.cursor.execute(
            """INSERT INTO Slots(moment, start, end) values (%s, %s, %s)""", (moment, start, end))
        self.commit()
        return True


    def select_slots(self):
        """SELECT SLOTS"""
        self.cursor.execute(
            """SELECT * FROM Slots""")
        return self.cursor.fetchall()
    

    def free_slots(self, date):
        """Show free slots for a given date"""
        self.cursor.execute(
            """SELECT moment FROM Slots WHERE id_slot NOT IN (SELECT slot FROM Bookings WHERE date = %s);""", (date,))
        return self.cursor.fetchall()
    

