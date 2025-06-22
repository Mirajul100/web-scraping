import requests
import selectorlib
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class Event:
# Scraping website 
    def scrap (self ,url):
        response = requests.get(url= url , headers= HEADERS)
        source = response.text
        return source

    def extract (self , source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tour"]
        return value

class Store:
    def __init__(self , database_path):
        # Connect the sql database
        self.connection = sqlite3.connect(database_path)

    def store(self , extract):
        row = extract.split(",")
        row = [item.strip() for item in row]
        cursor = self.connection.cursor()
        # Inserted the information to sql database
        cursor.execute("INSERT INTO records VALUES (?,?,?)" , row)
        self.connection.commit()


    def read(self , extract):
        row = extract.split(",")
        row = [item.strip() for item in row]
        band , city , date = row
        cursor = self.connection.cursor()
        # Fetch the database information using query
        cursor.execute("SELECT * FROM records WHERE band=? AND city = ? AND date = ?" , (band , city , date))
        rows = cursor.fetchall()
        print (rows)
        return rows
