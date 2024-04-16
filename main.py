# Importation des bibliothèques nécessaires
from datetime import datetime

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

def main():
    while True:
        print("\nAgenda Électronique")
        print("1. Ajouter un rendez-vous")
        print("2. Voir les rendez-vous")
        print("3. Quitter")
        choice = input("Choisissez une option : ")
        if choice == '1':
            date = input("Entrez la date (JJ-MM-AAAA) : ")
            time = input("Entrez l'heure (HH:MM) : ")
            description = input("Description du rendez-vous : ")
            add_appointment(date, time, description)
        elif choice == '2':
            view_appointments()
        elif choice == '3':
            break
        else:
            print("Option non reconnue, veuillez réessayer.")

if __name__ == "__main__":
    main()

