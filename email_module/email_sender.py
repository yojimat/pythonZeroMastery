import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # os.path

html = Template(Path("index.html").read_text())

email = EmailMessage()
email["from"] = "Vinicius Neves"
email["to"] = "email@gmail.com"
email["subject"] = "Testando envio de e-mail"

email.set_content(html.substitute({"nome": "Vinicius", "sobrenome": "Neves"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email@gmail.com", "****")
    smtp.send_message(email)
    print("Mensagem enviada")
