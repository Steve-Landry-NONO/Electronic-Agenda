# agenda_gui.py
import tkinter as tk
from tkinter import messagebox, ttk
from core import add_appointment, add_birthday, add_note, view_appointments, view_birthdays, view_notes


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Électronique")
        self.root.geometry("600x400")

        # Tabs
        self.tabs = ttk.Notebook(root)
        self.tab_appointments = ttk.Frame(self.tabs)
        self.tab_birthdays = ttk.Frame(self.tabs)
        self.tab_notes = ttk.Frame(self.tabs)
        self.tabs.add(self.tab_appointments, text="Rendez-vous")
        self.tabs.add(self.tab_birthdays, text="Anniversaires")
        self.tabs.add(self.tab_notes, text="Notes")
        self.tabs.pack(expand=1, fill="both")

        # Rendez-vous Tab
        self.setup_appointment_tab()
        # Anniversaires Tab
        self.setup_birthday_tab()
        # Notes Tab
        self.setup_note_tab()

    def setup_appointment_tab(self):
        """Configure l'onglet des rendez-vous."""
        frame_form = ttk.Frame(self.tab_appointments)
        frame_form.pack(pady=10)

        ttk.Label(frame_form, text="Date (JJ-MM-AAAA) :").grid(row=0, column=0, sticky="e")
        self.entry_appointment_date = ttk.Entry(frame_form)
        self.entry_appointment_date.grid(row=0, column=1)

        ttk.Label(frame_form, text="Heure (HH:MM) :").grid(row=1, column=0, sticky="e")
        self.entry_appointment_time = ttk.Entry(frame_form)
        self.entry_appointment_time.grid(row=1, column=1)

        ttk.Label(frame_form, text="Description :").grid(row=2, column=0, sticky="e")
        self.entry_appointment_desc = ttk.Entry(frame_form)
        self.entry_appointment_desc.grid(row=2, column=1)

        ttk.Button(frame_form, text="Ajouter", command=self.add_appointment).grid(row=3, column=0, columnspan=2)

        self.tree_appointments = ttk.Treeview(self.tab_appointments, columns=("Date", "Description"), show="headings")
        self.tree_appointments.heading("Date", text="Date")
        self.tree_appointments.heading("Description", text="Description")
        self.tree_appointments.pack(fill="both", expand=True)

        self.update_appointments()

    def add_appointment(self):
        date = self.entry_appointment_date.get()
        time = self.entry_appointment_time.get()
        description = self.entry_appointment_desc.get()
        if date and time and description:
            try:
                add_appointment(date, time, description)
                self.update_appointments()
                messagebox.showinfo("Succès", "Rendez-vous ajouté avec succès !")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur : {e}")
        else:
            messagebox.showwarning("Avertissement", "Veuillez remplir tous les champs.")

    def update_appointments(self):
        for i in self.tree_appointments.get_children():
            self.tree_appointments.delete(i)
        for appointment in view_appointments():
            date = appointment['date_time'].strftime("%d-%m-%Y %H:%M")
            desc = appointment['description']
            self.tree_appointments.insert("", "end", values=(date, desc))

    def setup_birthday_tab(self):
        """Configure l'onglet des anniversaires."""
        frame_form = ttk.Frame(self.tab_birthdays)
        frame_form.pack(pady=10)

        ttk.Label(frame_form, text="Date (JJ-MM) :").grid(row=0, column=0, sticky="e")
        self.entry_birthday_date = ttk.Entry(frame_form)
        self.entry_birthday_date.grid(row=0, column=1)

        ttk.Label(frame_form, text="Nom :").grid(row=1, column=0, sticky="e")
        self.entry_birthday_name = ttk.Entry(frame_form)
        self.entry_birthday_name.grid(row=1, column=1)

        ttk.Button(frame_form, text="Ajouter", command=self.add_birthday).grid(row=2, column=0, columnspan=2)

        self.tree_birthdays = ttk.Treeview(self.tab_birthdays, columns=("Date", "Nom"), show="headings")
        self.tree_birthdays.heading("Date", text="Date")
        self.tree_birthdays.heading("Nom", text="Nom")
        self.tree_birthdays.pack(fill="both", expand=True)

        self.update_birthdays()

    def add_birthday(self):
        date = self.entry_birthday_date.get()
        name = self.entry_birthday_name.get()
        if date and name:
            try:
                add_birthday(date, name)
                self.update_birthdays()
                messagebox.showinfo("Succès", "Anniversaire ajouté avec succès !")
            except Exception as e:
                messagebox.showerror("Erreur", f"Erreur : {e}")
        else:
            messagebox.showwarning("Avertissement", "Veuillez remplir tous les champs.")

    def update_birthdays(self):
        for i in self.tree_birthdays.get_children():
            self.tree_birthdays.delete(i)
        for birthday in view_birthdays():
            date = birthday['date'].strftime("%d-%m")
            name = birthday['name']
            self.tree_birthdays.insert("", "end", values=(date, name))

    def setup_note_tab(self):
        """Configure l'onglet des notes."""
        frame_form = ttk.Frame(self.tab_notes)
        frame_form.pack(pady=10)

        ttk.Label(frame_form, text="Titre :").grid(row=0, column=0, sticky="e")
        self.entry_note_title = ttk.Entry(frame_form)
        self.entry_note_title.grid(row=0, column=1)

        ttk.Label(frame_form, text="Contenu :").grid(row=1, column=0, sticky="e")
        self.entry_note_content = ttk.Entry(frame_form)
        self.entry_note_content.grid(row=1, column=1)

        ttk.Button(frame_form, text="Ajouter", command=self.add_note).grid(row=2, column=0, columnspan=2)

        self.tree_notes = ttk.Treeview(self.tab_notes, columns=("Titre", "Contenu"), show="headings")
        self.tree_notes.heading("Titre", text="Titre")
        self.tree_notes.heading("Contenu", text="Contenu")
        self.tree_notes.pack(fill="both", expand=True)

        self.update_notes()

    def add_note(self):
        title = self.entry_note_title.get()
        content = self.entry_note_content.get()
        if title and content:
            add_note(title, content)
            self.update_notes()
            messagebox.showinfo("Succès", "Note ajoutée avec succès !")
        else:
            messagebox.showwarning("Avertissement", "Veuillez remplir tous les champs.")

    def update_notes(self):
        for i in self.tree_notes.get_children():
            self.tree_notes.delete(i)
        for note in view_notes():
            self.tree_notes.insert("", "end", values=(note['title'], note['content']))


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
