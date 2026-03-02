class User:
    def __init__(self, firstname, lastname, email, call_number, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.call_number = call_number
        self.password = password

    
    def __str__(self):
        return f"{self.email}| Motif : {self.firstname} | {self.lastname} | {self.call_number}"