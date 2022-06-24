from flask import Flask
from flask_mail import Mail, Message

app = Flask("EmailService") # pick the name
mail = Mail(app)



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nnamutual@gmail.com'
app.config['MAIL_PASSWORD'] = 'pwjlcqdeaktkszdz'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
  msg = Message('Hello from the other side!', sender =   'nnamutal@gmail.com', recipients = ['amrale.netra@gmail.com'])
  msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
  mail.send(msg)
  return "Message sent!"

if __name__ == '__main__':
   app.run(debug = True)

# sender_address = "nnamutual@gmail.com" # Replace this with your Gmail address
# receiver_address = "netscho6@gmail.com" # Replace this with any valid email address
# account_password = "mutualnna" # Replace this with your Gmail account password
# subject = "Test Email using Python"
# body = "Hello from AskPython!\n\nHappy to hear from you!\nWith regards,\n\tDeveloper"
# # Endpoint for the SMTP Gmail server (Don't change this!)
# smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
# smtp_server.ehlo()

# smtp_server.ehlo()
# # Login with your Gmail account using SMTP
# smtp_server.login(sender_address, account_password)
# # Let's combine the subject and the body onto a single message

# from_add = ("From: "+ sender_address)
# msg = "\r\n".join([
#   from_add,
#   ("To: "+ receiver_address),
#   "Subject: "+subject,
#   "",
#   "Why, oh why"
#   ])
# message = f"Subject: {subject}\n\n{body}"
# # We'll be sending this message in the above format (Subject:...\n\nBody)
# smtp_server.sendmail(sender_address, receiver_address, msg)
# # Close our endpoint
# smtp_server.close()