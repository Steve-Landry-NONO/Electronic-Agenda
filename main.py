# Importation des bibliothèques nécessaires
from datetime import datetime


""" ********************************************** Gestion des rendez-vous ********************************************************** """

# Base de données en mémoire pour stocker les rendez-vous
appointments = []

def add_appointment(date_str, time_str, description):
    """Ajoute un nouveau rendez-vous à la liste."""
    date_time_str = f"{date_str} {time_str}"
    date_time = datetime.strptime(date_time_str, "%d-%m-%Y %H:%M")
    appointments.append((date_time, description))
    print("Rendez-vous ajouté avec succès !")

def view_appointments():
    """Affiche tous les rendez-vous triés par date et heure."""
    for appointment in sorted(appointments):
        print(f"{appointment[0].strftime('%d-%m-%Y %H:%M')} - {appointment[1]}")


    """ *************************************** Gestion des anniversaires ******************************************************* """

birthdays = []

def add_birthday(date_str, name):
    """Ajoute un anniversaire à la liste."""
    date = datetime.strptime(date_str, "%d - %m")
    birthdays.append((date, name))
    print("Anniversaire ajouté avec succès !")

def view_birthdays():
    """Affiche les anniversaires à venir dans le mois courant."""
    current_month = datetime.now().month
    for birthday in birthdays:
        if birthday[0].month == current_month:
            print(f"{birthday[0].strftime('%d - %m')} - {birthday[1]}")


""" ******************************************** Gestion des notes personnelles ****************************************************"""

notes = []
def add_note(title, content):
    """ Ajoute une nouvelle note à la liste. """
    note = {'title': title, 'content': content}
    notes.append(note)
    print("Note ajoutée avec succès !")

def view_notes():
    """ Affiche toutes les enregistrées."""
    if not notes:
        print("Aucune note enregistrée")
    else:
        for note in notes:
            print(f"Titre: {note['title']}\nContenu: {note['content']}\n")
def main():
    while True:
        print("\nAgenda Électronique")
        print("1. Ajouter un rendez-vous")
        print("2. Voir les rendez-vous")
        print("3. Ajouter un anniversaire")
        print("4. Voir les anniversaire")
        print("5. Ajouter une note")
        print("6. Voir les notes")
        print("7. Quitter")
        choice = input("Choisissez une option : ")
        if choice == '1':
            date = input("Entrez la date (JJ-MM-AAAA) : ")
            time = input("Entrez l'heure (HH:MM) : ")
            description = input("Description du rendez-vous : ")
            add_appointment(date, time, description)
        elif choice == '2':
            view_appointments()
        elif choice == '3':
            date = input("Entrer la date (JJ-MM) : ")
            name = input("Entrer le nom : ")
            add_birthday(date, name)
        elif choice == '4':
            view_birthdays()
        elif choice == '5':
            title = input("Entrez le titre de la note :")
            content = input("Entrez le contenu de la note :")
            add_note(title, content)
        elif choice == '6':
            view_notes()
        elif choice == '7':
            break
        else:
            print("Option non reconnue, veuillez réessayer.")

if __name__ == "__main__":
    main()

