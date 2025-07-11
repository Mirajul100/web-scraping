import requests
import selectorlib
import time
import sqlite3

connection = sqlite3.connect("data.db")

time_url = "http://programmer100.pythonanywhere.com/"

file_path = "textFile/time.txt"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

temp = time.strftime("%Y.%m.%d")

class Temperature:
    def time_scrap(self , time_url):
        time_response = requests.get(time_url , headers=HEADERS)
        time_source = time_response.text
        return time_source

    def time_ex(self , time_source):
        time_ext = selectorlib.Extractor.from_yaml_file("extract.yaml")
        time_sou = time_ext.extract(time_source)["time"]
        return time_sou
