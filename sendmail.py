import requests
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to fetch OHLC data
def fetch_ohlc_data(ticker, api_key):
    url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['results'][0] if 'results' in data and data['results'] else None
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def send_email(subject, message, sender, password, recipient):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.example.com', 587)  # Update with your SMTP details
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, msg.as_string())
    server.quit()

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <TICKER>")
        sys.exit(1)

    ticker = sys.argv[1]
    api_key = 'Pgq1zXTF7aq8RrEVuGwrAUm3dN4z7vkN'
    ohlc_data = fetch_ohlc_data(ticker, api_key)

# Open, High, Low, Close
    if ohlc_data:
        sender = 'your-email@example.com'
        password = 'your-email-password'
        recipient = 'recipient-email@example.com'
        subject = f'Daily OHLC Data for {ticker}'
        body = f"Open: {ohlc_data['o']}\nHigh: {ohlc_data['h']}\nLow: {ohlc_data['l']}\nClose: {ohlc_data['c']}\n"
        send_email(subject, body, sender, password, recipient)
    else:
        print("No data found for the given ticker.")

if __name__ == "__main__":
    main()
