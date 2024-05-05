# DOCUMENTATION
## STOCK AUTOMATIZATION
#### made by Naima Cavegn, Zachary Jenkins <br><br>

## PROJECT DESCRIPTION:
This repository is for an automation project of module 122 Bash. <br>
The assignment was as LB2 project work to create an automation with server and client, also taking security into account.<br>
Everyone in the team should have their own customized code, but ideas and inspirations can be shared. <br>
It's an automation for stocks that tracks the increase and decrease of the stocks and updates them in certain time intervals.<br>
Users can enter their e-mail and receive the data from the stocks accordingly.<br>
The automation is useful for those who are interested in the market and stocks, as they are directly notified when something happens. 
All data is retrieved from an API and updated at certain frequency, then stored in a database.<br>
Our project also takes security into consideration, which is why we have login details that can be found in the installation section.<br>

## Meilensteine
A: We discussed the Projekt with our teacher and filled out the document with the "Anforderungsdefinition". In a second step we created an UML  activity diagram. <br>
ADD Activity Diagram
B: Implementation of the solution
C: We've created this GitHub Repository with three branches. One for Zachary, one for Naima and the main branch. However, we had a little trouble working with the branches because we haven't done this before. However, we tried our best.

## PROJECT START AND END:
We started the project on ... and had to work on it at school a total of 4 times. That's about 16 hours in altogether and the rest at home. The project was presented on 6.5.24 with a demo and the documentation.

## PROJECT RESULTS:
Our project can send emails and checks the status of the API with the latest data.

## TEAM:
Naima Cavegn and Zachary Jenkins.We basically wrote our code on our own, but we were allowed to support each other with questions and project development.

## DEADLINE:
The project deadline was May 6, when we also had to hand in our project.

## INSTALLATION:
To use our project yourself, you can use the following instructions with the data and set up the project locally.<br>

## Code Zachary
Here you can see the code that we have done:
```
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import logging

# Set up logging
logging.basicConfig(filename='stock_price_updates.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Polygon API credentials
api_key = 'Pgq1zXTF7aq8RrEVuGwrAUm3dN4z7vkN'

# Email credentials
sender_email = "tbzmodul@gmail.com"
sender_password = "TBZmodul1234!!"
recipient_email = "tbzmodul@gmail.com"

# List of stock tickers to track
tickers = ["AAPL", "MSFT"]  # Example tickers


def send_email(body, subject="Stock Price Information for Multiple Tickers"):
    """Send an email with the given body and subject."""
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create SMTP session for sending the mail
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error("Failed to send email. Error: %s", str(e))
    finally:
        server.quit()


def fetch_data_and_send_email():
    body = ""
    for ticker in tickers:
        try:
            url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={api_key}'
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses

            stock_info = response.json()
            if 'results' in stock_info and stock_info['results']:
                prices = stock_info['results'][0]
                body += f"{ticker}: Open: {prices['o']}, High: {prices['h']}, Low: {prices['l']}, Close: {prices['c']}\n"
            else:
                body += f"{ticker}: No data found.\n"

        except requests.exceptions.HTTPError as e:
            logging.error("HTTP Error for %s: %s", ticker, str(e))
            body += f"{ticker}: HTTP Error retrieving data.\n"
        except requests.exceptions.RequestException as e:
            logging.error("Request Exception for %s: %s", ticker, str(e))
            body += f"{ticker}: Request Exception retrieving data.\n"

    if body:
        send_email(body)


# Schedule the email to be sent every 5 minutes
schedule.every(5).minutes.do(fetch_data_and_send_email)

# Infinite loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
