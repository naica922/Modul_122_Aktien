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