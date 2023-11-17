import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to send an email
def send_email(name, age, funcao):
    # Your email and password
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    # Recipient's email address
    recipient_email = "recipient_email@example.com"

    # Create an email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "User Information"

    # Email body
    body = f"Nome: {name}\nIdade: {age}\nFunção: {funcao}"
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

if __name__ == '__main__':
    name = input("Qual é o seu nome? ")
    age = input("Qual é a sua idade? ")
    funcao = input("Qual é a sua função? ")

    # Display the entered information
    print(f"Nome: {name}")
    print(f"Idade: {age}")
    print(f"Função: {funcao}")

    # Send an email with the information
    send_email(name, age, funcao)