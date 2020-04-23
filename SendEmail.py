import sendgrid
# from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Content


def send_email(email, name):
    API_KEY = "***************"
    SUBJECT = "Welcome"
    BODY = "Hi {name}"
    body = BODY.format(name=name)

    message = Mail(
        from_email="************",
        to_emails=email,
        subject=SUBJECT,
        html_content=Content("text/plain", BODY.format(name=name)))
    print(message)
    try:
        sg = sendgrid.SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except:
        print("Sasi")


send_email("mashaasham@gmail.com", "Mariia")

