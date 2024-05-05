
# Code and documentation Zachary
Here you can see the code that I have done:
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
sender_password = "TBZmodul1234!"
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


# Schedule the email to be sent every 10 minutes
schedule.every(10).minutes.do(fetch_data_and_send_email)

# Infinite loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute

```

### Imports
So as you can see we have some imports so lets go through every single one of them:
```
import requests
```
This library allows you to send HTTP requests easily.
```
import time
```
This module provides various time-related functions.
```
import json
```
This module allows you to work with JSON (JavaScript Object Notation) data.
```
import smtplib
```
This module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.
```
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
```
These are classes from the email.mime module that allow you to create multipart email messages with text and attachments.
```
import schedule
```
This import works kind of like cronjob. You can set a timer in it.

### Email config
In this part we have set up the email which recives the mail and the one which sends it. We also had to manage the security part on google and had to get a code which alows us to use our gmail in this script.
```
sender_email = "tbzmodul@gmail.com"
sender_password = "TBZmodul1234!"
recipient_email = "tbzmodul@gmail.com"
```
### API endpoint
With this next part we are getting the endpoint for the information of the stocks. With the help of the API key I can acces the endpoint
```
 url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={api_key}'
            response = requests.get(url)
            response.raise_for_status()
api_key = 'Pgq1zXTF7aq8RrEVuGwrAUm3dN4z7vkN'
```
### Creating the email
Now it creates the email and in the next step it will be sent. The error messages are also logged.
```
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
```
### Fetching data and sending the email
Now in this step it fetches the current data and sends the email with the data as the body.
```
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
```
### Schedule (cronjob)
This is the last part of the script and we used the schedule to make the program send an email every 10 minutes.
```
# Schedule the email to be sent every 10 minutes
schedule.every(10).minutes.do(fetch_data_and_send_email)

# Infinite loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
```
