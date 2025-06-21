import requests
import selectorlib
import sqlite3

# Connect the sql database
connection = sqlite3.connect("data.db")

URL = "http://programmer100.pythonanywhere.com/tours/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Scraping website 
def scrap (url):
    response = requests.get(url= url , headers= HEADERS)
    source = response.text
    return source

def extract (source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tour"]
    return value

def store(extract):
    row = extract.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    # Inserted the information to sql database
    cursor.execute("INSERT INTO records VALUES (?,?,?)" , row)
    connection.commit()

def read(extract):
    row = extract.split(",")
    row = [item.strip() for item in row]
    band , city , date = row
    cursor = connection.cursor()
    # Fetch the database information using query
    cursor.execute("SELECT * FROM records WHERE band=? AND city = ? AND date = ?" , (band , city , date))
    rows = cursor.fetchall()
    return rows
