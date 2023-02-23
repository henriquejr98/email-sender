import smtplib
import os
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import schedule
import time


# Set up logging
logging.basicConfig(filename="email_sender.log", level=logging.INFO)

# Define email addresses and credentials
sender_email = "your_email_address"
password = "your_email_password"

# Define message parameters
subject = "Daily Report"
body = "Please find attached the daily report."
html = """\
<html>
  <body>
    <p>{}</p>
  </body>
</html>
""".format(body)

# Define list of recipients and report file path
recipients = ["recipient1@example.com", "recipient2@example.com"]
report_file_path = "/path/to/report/file"

def send_email():
    # Create message object
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["Subject"] = subject

    # Attach message parts
    part1 = MIMEText(body, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    # Attach report file
    with open(report_file_path, "rb") as f:
        report_file = MIMEApplication(f.read(), _subtype="xlsx")
        report_file.add_header("Content-Disposition", "attachment", filename=os.path.basename(report_file_path))
        message.attach(report_file)

    # Connect to email server and send message to each recipient
    for recipient in recipients:
        message["To"] = recipient
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient, message.as_string())
                logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Error sending email to {recipient}: {str(e)}")

# Schedule the script to run daily at 6:00 AM
schedule.every().day.at("06:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(1)
