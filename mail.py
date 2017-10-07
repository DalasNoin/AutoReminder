import sendgrid
from keys import sendgrid_apikey
from sendgrid.helpers.mail import *
sg = sendgrid.SendGridAPIClient(apikey=sendgrid_apikey)
from_email= Email("AutoReminder@Random.com")

def send(to, subject, con):
    to_email = Email(to)
    content = Content("text/html", con) #text/plain
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code
