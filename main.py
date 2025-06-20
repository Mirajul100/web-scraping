import requests
import selectorlib
import time
from send_email import send_mail

URL = "http://programmer100.pythonanywhere.com/tours/"
time_url = "http://programmer100.pythonanywhere.com/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

temp = time.strftime("%Y.%m.%d")

def scrap (url):
    response = requests.get(url= url , headers= HEADERS)
    source = response.text
    return source

def extract (source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tour"]
    return value

def time_scrap(time_url):
    time_response = requests.get(time_url , headers=HEADERS)
    time_source = time_response.text
    return time_source

def time_ex(time_source):
    time_ext = selectorlib.Extractor.from_yaml_file("extract.yaml")
    time_sou = time_ext.extract(time_source)["time"]
    return time_sou

def store(extract):
    with open ("data.txt" , "a") as file:
        file.write(extract + "\n")

def read(extract):
    with open ("data.txt" , "r") as file:
        DATA = file.read()
        return DATA

def store_time(time_ex):
    with open ("time.txt" , "a") as file:
        file.write(f"{temp},{time_ex}" + "\n")

    
def time_read (time_ex):
    with open ("time.txt" , "r") as file:
        return file.read()

if __name__ == "__main__":
    scraps = scrap(URL)
    extracted = extract(scraps)
    print (extracted)

    time_scraps = time_scrap(time_url)
    t_time = time_ex(time_scraps)
    print (t_time)

    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store_time(time_ex=t_time)
            store(extract=extracted)
            massage = f"""\
            Tour planner:

            Hey you have new massage
            {extracted}
            World temperature : {t_time}
            """
            send_mail(massage)
            print ("massage send successfully")
            