""" *************************** Gestion des notifications ******************************************** """

from plyer import notification
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def notify_appointment_desktop(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,  # Optionnel: chemin vers un fichier icône
        timeout=10  # Temps d'affichage de la notification
    )
def send_email(subject, message, to_email):
    from_email = "nonostevelandry@gmail.com"
    from_password = "a1b2c3d4"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Port SMTP pour la plupart des services

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def notify_user(appointment):
    title = 'Rappel de Rendez-vous'
    message = f"Vous avez un rendez-vous : {appointment['description']} à {appointment['date_time'].strftime('%Y-%m-%d %H:%M')}"
    notify_appointment_desktop(title, message)
    send_email(title, message, "stevelandryk89@gmail.com")

def check_for_upcoming_appointments():
    now = datetime.datetime.now()
    for appointment in appointments:
        appointment_time = appointment['date_time']
        if (appointment_time - now).total_seconds() < 3600:  # Rappel 1 heure avant
            notify_user(appointment)