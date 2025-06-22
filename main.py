from tour import Event , Store , URL
from world_temp import Temperature, time_url
from send_email import send_mail
import sqlite3

# Connect the sql database
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

if __name__ == "__main__":
    event = Event()
    scraps = event.scrap(URL)
    extracted = event.extract(scraps)
    print (extracted)

    temperature = Temperature()
    time_scraps = temperature.time_scrap(time_url)
    t_time = temperature.time_ex(time_scraps)
    print (t_time)

    if extracted != "No upcoming tours":
        stores = Store(database_path="data.db")
        rows = stores.read(extracted )
        if not rows :
            stores.store(extract=extracted)
            massage = f"""\
            Tour planner:

            Hey you have new massage
            {extracted}
            World temperature : {t_time}
            """
            send_mail(massage)
            print ("massage send successfully")
            