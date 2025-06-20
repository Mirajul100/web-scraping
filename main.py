from tour import scrap , extract , store , read , URL
from world_temp import time_scrap , time_read , time_ex , store_time , time_url
from send_email import send_mail

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
            