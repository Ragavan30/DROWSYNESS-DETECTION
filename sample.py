from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Change this to your email provider's SMTP server
app.config['MAIL_PORT'] = 587  # Change this to the port of your email provider's SMTP server
app.config['MAIL_USE_TLS'] = True  # Enable TLS, set to False if using SSL
app.config['MAIL_USERNAME'] = 'hariviki7895@gmail.com'  # Your email address
app.config['MAIL_PASSWORD'] = 'kmvwrwphnjsfamtu'  # Your email password

mail = Mail(app)

@app.route('/')
def index():
    return 'Welcome to Flask Mail Example'

@app.route('/send_mail')
def send_mail():
    msg = Message( 
                'Hello', 
                sender ='hariviki7895@gmail.com', 
                recipients = ['regubalan70@gmail.com'] 
               ) 
    msg.body = 'Hello Flask message sent from Flask-Mail'
    mail.send(msg) 
    return 'Sent'

if __name__ == '__main__':
    app.run(debug=True)
