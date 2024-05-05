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

## MILESTONES
A: We discussed the Projekt with our teacher and filled out the document with the "An forderungsdefinition". In a second step we created an UML  activity diagram. <br>
![image](https://github.com/naica922/Modul_122_Aktien/assets/150661049/d998ba72-3e48-4ea9-b3ba-16963a2ba9c3)
<br>
B: Implementation of the solution <br>
C: We've created this GitHub Repository with three branches. One for Zachary, one for Naima and the main branch. However, we had a little trouble working with the branches because we haven't done this before. However, we tried our best.

## PROJECT START AND END:
We started the project approximately on the 26.03.24 and had to work on it at school a total of 4 times. <br>
That's about 16 hours in altogether and the rest at home. <br>
The project was presented on 6.5.24 with a demo and the documentation.

## PROJECT RESULTS:
Our project can send emails and checks the status of the API with the latest data.

## TEAM:
Naima Cavegn and Zachary Jenkins
We basically wrote our code on our own, but we were allowed to support each other with questions and project development.

## DEADLINE:
The project deadline was May 6, when we also had to hand in our project.

## INSTALLATION:
To use our project yourself, you can use the following instructions with the data and set up the project locally.<br>
We both created our own documentation for the setup which you can find in this markdown or in the branches.

## Code and documentation Zachary
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
