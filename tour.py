import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"

file_path = "textFile/data.txt"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def scrap (url):
    response = requests.get(url= url , headers= HEADERS)
    source = response.text
    return source

def extract (source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tour"]
    return value

def store(extract):
    with open (file_path , "a") as file:
        file.write(extract + "\n")

def read(extract):
    with open (file_path , "r") as file:
        DATA = file.read()
        return DATA