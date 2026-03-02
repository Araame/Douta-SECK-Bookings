from auth import Auth
from manager import Booking_manager
from slot import Slots
from db import DatabaseManager

class Menu:
    def __init__(self):
        self.auth = Auth()
        self.bm = Booking_manager()
        self.db = DatabaseManager()


    def auth_menu(self):
        print("1. Sign up | 2. Sign in | 3. Exit")
        choice = int(input("Choice : "))

        match choice:
            case 1:
                self.auth.signup()
            case 2:
                user = self.auth.signin()
                if user :
                    self.main_menu(user)

    def main_menu(self, user):
        """Menu for users"""

        if user["role"] == 1:
            while True:
                print("\n=== Welcome to Douta SECK ===")
                print("1. Book my day \n " \
                "2. Show my bookings \n" \
                "3. Cancel a booking \n" \
                "0. Log out")

                choice = input("\nChoice :")

                match choice :
                    case "1":
                        self.bm.make_booking(user["id_staff"])
                    case "2":
                        for book in self.db.select_user_bookings(user["id_staff"]):
                            print(book)
                    case "3":
                        if self.bm.cancel_booking():
                            print("Booking cancelled")
                        
                    case "4":
                        exit()
                    case _ :
                        print("Invalid option")
        else:
            while True:
                print("\n=== Welcome to Douta SECK ===")
                print("1. Book my day \n " \
                "2. Show my bookings \n" \
                "3. Show all bookings \n" \
                "4. Show avalaible slots \n" \
                "5. Cancel a booking \n" \
                "6. Create a slot \n" \
                "7. Show slots \n" \
                "8. Generate CSV file"
                "0. Log out \n")

                choice = input("\nChoice :")

                match choice :
                    case "1":
                        self.bm.make_booking(user["id_staff"])
                    case "2":
                        self.bm.show_user_bookings(user["id_staff"])
                    case "3":
                        for book in self.db.select_all_bookings():
                            print(book)
                    case "4":
                        for slot in self.bm.show_free_slots():
                            print(slot)
                    case "5":
                        self.db.cancel_booking()
                    case "6":
                        self.bm.create_slot()
                    case "7":
                        self.db.select_slots()
                    case "8":
                        self.bm.generate_csv()
                    case "0":
                        exit()
                    case _ :
                        print("Invalid option")

menu = Menu()
menu.auth_menu()
                    
                
                
