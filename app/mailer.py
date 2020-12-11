from app import mail

from flask_mail import Message

def send_mail(content):
  msg = Message(
    "[kevinkoh.dev] {}".format(content['subject']),
    sender="kevin@koshilabs.com",
    recipients=["kevin.koh.dev@gmail.com"]
  )
  msg.body = "from: {name}\nemail: {email}\nphone:{phone}\nmessage:\n{message}".format(
    name=content['name'],
    email=content['email'],
    phone=content['tel'],
    message=content['message']
  )

  mail.send(msg)
