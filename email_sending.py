''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib
from dotenv import dotenv_values
from email.message import EmailMessage

def start_server( host, port ):
    server = smtplib.SMTP( host, port )
    return server

def login( server, login, password ):
    server.ehlo()
    server.starttls()
    server.login( login, password )

def create_email( sender, receiver, subject, body ):
    email_msg = EmailMessage()
    email_msg[ 'From' ] = sender
    email_msg[ 'To' ] = receiver
    email_msg[ 'subject' ] = subject
    email_msg.set_content( body )
    return email_msg

def send_email( server, sender, receiver, email_created ):
    server.sendmail( sender, receiver, email_created.as_string() )


if __name__ == '__main__':
    env_config = dotenv_values( '.env' ) # This will return a dict with our keys in .env.
    host = 'smtp.gmail.com'
    port = '587'
    sender_email = 'henrique.sender@gmail.com'
    server = start_server( host, port )
    login( server, sender_email, env_config[ 'APP_PASSWORD' ] )
    created = create_email( sender_email, sender_email, 'Test', 'This is a test!' )
    send_email( server, sender_email, sender_email, created )

