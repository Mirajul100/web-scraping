from tour import scrap , extract , store , read , URL
from world_temp import time_scrap , time_ex , time_url
from send_email import send_mail
import sqlite3

# Connect the sql database
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

if __name__ == "__main__":
    scraps = scrap(URL)
    extracted = extract(scraps)
    print (extracted)

    time_scraps = time_scrap(time_url)
    t_time = time_ex(time_scraps)
    print (t_time)

    if extracted != "No upcoming tours":
        rows = read(extracted )
        if not rows :
            store(extract=extracted)
            massage = f"""\
            Tour planner:

            Hey you have new massage
            {extracted}
            World temperature : {t_time}
            """
            send_mail(massage)
            print ("massage send successfully")
            