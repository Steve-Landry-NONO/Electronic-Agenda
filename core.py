# agenda_core.py
from datetime import datetime

appointments = []
birthdays = []
notes = []

def add_appointment(date_str, time_str, description):
    """Ajoute un rendez-vous à la liste."""
    date_time_str = f"{date_str} {time_str}"
    date_time = datetime.strptime(date_time_str, "%d-%m-%Y %H:%M")
    appointments.append({'date_time': date_time, 'description': description})

def view_appointments():
    """Renvoie une liste de rendez-vous triés par date."""
    return sorted(appointments, key=lambda x: x['date_time'])

def add_birthday(date_str, name):
    """Ajoute un anniversaire à la liste."""
    date = datetime.strptime(date_str, "%d-%m")
    birthdays.append({'date': date, 'name': name})

def view_birthdays():
    """Renvoie une liste d'anniversaires dans le mois courant."""
    current_month = datetime.today().month
    return [b for b in birthdays if b['date'].month == current_month]

def add_note(title, content):
    """Ajoute une note à la liste."""
    notes.append({'title': title, 'content': content})

def view_notes():
    """Renvoie une liste de toutes les notes."""
    return notes
