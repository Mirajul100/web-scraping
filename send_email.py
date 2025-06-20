import smtplib , ssl

url = "qwiu avhu zpog aljj"

def send_mail(massage):
    host = "smtp.gmail.com"
    port = 465

    user = "python3436@gmail.com"
    receiver = "python3436@gmail.com"
    password = url

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host , port=port , context=context) as server:
        server.login(user=user , password=password)
        server.sendmail(user , receiver , massage)
        