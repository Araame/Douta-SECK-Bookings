import getpass
import bcrypt
from db import DatabaseManager
from user import User



class Auth:
    def __init__(self):
        self.db = DatabaseManager()

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        

    def signup(self):
            try:
                firstname = input("Firstname : ")
                lastname = input("Lastname : ")
                email = input("Email : ")
                call_number = input("Call number : ")
                password = getpass.getpass("Password : ")
                verified_password = getpass.getpass("Password (verified) : ")
                user = User(firstname, lastname, email, call_number, password)
                if password != verified_password:
                    print("Password doesn't match")

                if self.db.insert_user(user.firstname, user.lastname, user.email, user.call_number, self.hash_password(user.password)):
                    self.signin()

                    return True
                
            except Exception as e:
                
                self.db.connector.rollback()
                print(f"Error : {e}")


    def signin(self):
        while True:
            try:
                email = input("Email : ")
                password = getpass.getpass("Password : ")
                row = self.db.verify_credentials(email, password)

                if row:
                    print(f"Welcome {row["firstname"]}!")
                    return row
                
                else:
                    
                    print("Invalid credentials")

            except ValueError:
                print("Error occured")
                raise
            




