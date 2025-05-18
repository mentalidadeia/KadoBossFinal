import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from configs.credentials import EMAIL_ADDRESS, EMAIL_PASSWORD
from core.utils.logger import registrar_log

def enviar_email(destinatario, assunto, mensagem):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = destinatario
        msg['Subject'] = assunto

        msg.attach(MIMEText(mensagem, 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            servidor.sendmail(EMAIL_ADDRESS, destinatario, msg.as_string())

        registrar_log(f"E-mail enviado para {destinatario}.")
    except Exception as e:
        registrar_log(f"Erro ao enviar e-mail: {str(e)}")
