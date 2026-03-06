import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

def send_email(receiver, subject, content):
        
        message = Mail(
            from_email='aram171002@gmail.com',  
            to_emails=receiver,
            subject=subject,
            plain_text_content=content
        )

        try:
            sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
            sg.send(message)
            print("Email sent !")
        except Exception as e:
            print("Error :", e)

