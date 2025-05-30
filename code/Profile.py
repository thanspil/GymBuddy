# ----------------- PROFILE PAGE -----------------
# Profile.py

import tkinter as tk
from tkinter import messagebox

class ProfilePage(tk.Tk):
    def __init__(self, user_type="Χρήστης", email=None):
        super().__init__()
        self.title(f"Προφίλ {user_type}")
        self.geometry("400x300")

        tk.Label(self, text=f"Καλωσήρθες στο προφίλ σου, {user_type}!", font=("Arial", 16)).pack(pady=20)

        if email:
            tk.Label(self, text=f"Email: {email}").pack()

        tk.Label(self, text="Εδώ εμφανίζονται τα στοιχεία του λογαριασμού σου.").pack(pady=10)

        tk.Button(self, text="Αναζήτηση Υπηρεσιών", command=self.open_search).pack(pady=10)

        tk.Button(self, text="Έξοδος", command=self.destroy).pack(pady=20)

    def open_search(self):
        from Search import SearchScreen
        self.destroy()
        SearchScreen()



class ProfilePageAsTrainer(ProfilePage):
    def __init__(self, email=None, identity=None, cert=None):
        super().__init__(user_type="Γυμναστής")

        if identity:
            tk.Label(self, text=f"Ταυτότητα: {identity}").pack()
        if cert:
            tk.Label(self, text=f"Πιστοποίηση: {cert}").pack()