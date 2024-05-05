# DOCUMENTATION FOR USER AND ADMIN
## STOCK AUTOMATIZATION
#### by Naima Cavegn<br>

## PROJECT DESCRIPTION FOR USERS:
This repository is for an automation project of module 122 Bash. <br>
The assignment was as LB2 project work to create an automation with server and client, also taking security into the project.<br>
Everyone in the team should have their own customized code, but ideas and inspirations can be shared. <br>
It's an automation for stocks that tracks the values of the stocks and updates them in certain time intervals.<br>
Users can enter their e-mail and receive the data from the stocks accordingly.<br>
The automation is useful for those who are interested in the market and stocks, as they are directly notified when something happens. 
All data is retrieved from an API and updated at certain frequency.<br>
Our project also takes security into consideration, which is why we have login details that can be found in the code.<br> <br>

If you would like to use my project you can run the code and change the Email credentials to yours. Then you should receive the messages every several minutes.

## INSTALLATION GUIDE FOR ADMINS:
In order to use my project, I have created instructions for the corresponding setup and the development environment as described in the main branch.<br>

### 1. download Python<br>
To install the latest version of Python you can use the following link:
“https://www.python.org/?downloads”<br>
Once the setup has started, it is important that you specify to add Python to the system variables. <br>
Otherwise you may have problems later.<br>
You can test whether the download was successful in the terminal with the command “python --version”. <br>
It should show you which version you have and whether it exists at all. <br>

### 2. download development environment<br>
So that you can test the code, it is best if you get yourself a development environment. This could be VSCode, pyCharm etc.<br>
Choose the one that works best for you. Then create a new project there and add the code that is in this repository.<br>
It's best to name the file “stock_price_tracker.py”, because that's what I called mine and if you want it differently you have to modify the next steps.<br>

### 3. run project<br>
To test my project, open Windows Powershell or the CMD. Enter the following commands one after the other. <br>
cd “/your/location/stock_price_tracker.py” -> This command navigates to the corresponding directory, make sure that it has to be customized. <br>
python3 stock_price_tracker.py -> This command executes the code <br>
!If you get the error that the file could not be found then check for spelling mistakes and make sure that you go to the innermost folder otherwise the file will not be found!<br>

## CODE 
```
import requests # http
import smtplib # for sending an email
from email.mime.multipart import MIMEMultipart # to create emails
from email.mime.text import MIMEText
import schedule # planning exercises
import time # time functionality
import logging

# Set up logging file for status codes and errors
logging.basicConfig(filename='stock_price_updates.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Polygon API credentials
api_key = 'Pgq1zXTF7aq8RrEVuGwrAUm3dN4z7vkN'

# Email credentials
sender_email = "tbzmodul@gmail.com"
sender_password = "TBZmodul1234!!"
recipient_email = "tbzmodul@gmail.com"

# List of stock tickers to track
# send Email function sends email with the body and a subject
tickers = ["AAPL", "MSFT"]  # Example tickers

def send_stock_update_email(message_body, update_subject="Stock Price Updates"):
    """Send an email with the given body and subject."""
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = update_subject
    msg.attach(MIMEText(message_body, 'plain'))
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
        logging.error("Failed to send the email. Error: %s", str(e))
    finally:
        server.quit()

# calls the Data for every Symbol in the list and sends the mail with data
def fetch_stock_data_and_notify():
    message_content = ""
    for symbol in tickers:
        try:
            url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?adjusted=true&apiKey={api_key}'
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            stock_details = response.json()
            if 'results' in stock_details and stock_details['results']:
                prices = stock_info['results'][0]
                message_content += f"{symbol}: Open: {prices['o']}, High: {prices['h']}, Low: {prices['l']}, Close: {prices['c']}\n"
            else:
                message_content += f"{symbol}: No data found.\n"
        except requests.exceptions.HTTPError as e:
            logging.error("HTTP Error for %s: %s", symbol, str(e))
            message_content += f"{symbol}: HTTP Error retrieving data.\n"
        except requests.exceptions.RequestException as e:
            logging.error("Request Exception for %s: %s", symbol, str(e))
            message_content += f"{symbol}: Request Exception retrieving data.\n"
    if message_content:
        send_stock_update_email(message_content)

# Schedule email to be sent every 5 minutes
schedule.every(5).minutes.do(fetch_stock_data_and_notify)

# Infinite loop to run scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
```
### Explanation
At the top of my code are the imports. On the one side I have an import for the http requests which I need to be able to get data.<br>
I also have imports for sending emails which I have implemented with smtplib. These are the most important ones, the others still relate to the functionality with time etc. <br>
Next, I have code that sets up a logging system that writes status codes and error messages to a file called “stock_price_updates.log”. <br>
I have hardcoded my API key and login credentials. These can be changed and the API key customized to your own if you want. Since you also have to enter the password from the email, Zachary and I thought about creating a Gmail that we can both use for this project. <br>
The 'tickers' list contains the symbols of the stocks whose prices are to be tracked, for example “AAPL” for Apple and “MSFT” for Microsoft. <br>
The `send_stock_update_email` function is defined to send emails with a specific message text and subject. This function uses the `smtplib` library to establish a connection to the email server and send the email. Errors when sending the e-mail are logged. <br>
The `fetch_stock_data_and_notify` function is defined to get the stock data for each symbol in the list of tickers. It uses the `requests` library to retrieve data from an API. The data is then analyzed and an email with the quote details is prepared. Errors in retrieving the data are also logged. <br>
 The `schedule` library is used to call the `fetch_stock_data_and_notify` function every 5 minutes. This ensures that the stock data is regularly updated and emails are sent.<br>
In the end, an infinite loop is started that monitors the schedule and calls the appropriate functions. This enables continuous updating of the share data and the sending of e-mails. <br>
The loop checks the schedule for updates every 60 seconds.



