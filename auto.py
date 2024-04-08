import requests
import pymysql

# API und Datenbankdetails
api_key = 'Pgq1zXTF7aq8RrEVuGwrAUm3dN4z7vkN'
url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-01/2023-03-01?adjusted=true&sort=asc&limit=120'  # Beispiel-URL für AAPL
db_host = 'm122-server.local'
db_user = 'user01'
db_password = 'MaSq-01'
db_name = 'm122-server.local'

# Daten von der Polygon API abrufen
response = requests.get(url, headers={'Authorization': f'Bearer {api_key}'})
data = response.json()

# Verbindung zur MariaDB-Datenbank herstellen
conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
cursor = conn.cursor()

# Daten in die Datenbank einfügen
for item in data['results']:
    cursor.execute('''
    INSERT INTO stock_data (date, open, high, low, close, volume)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''', (item['t'], item['o'], item['h'], item['l'], item['c'], item['v']))

# Änderungen speichern und Verbindung schließen
conn.commit()
cursor.close()
conn.close()
