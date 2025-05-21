import tkinter as tk
from tkinter import messagebox

# Χρώματα και γραμματοσειρές
PURPLE = "#6A0DAD"
WHITE = "#ffffff"
BLACK = "#000000"
FONT_TITLE = ("Helvetica", 20, "bold")
FONT_LABEL = ("Helvetica", 11)
FONT_ENTRY = ("Helvetica", 11)

class LoginScreen:
    def __init__(self, master):
        self.master = master
        master.title("GymBuddy - Σύνδεση")
        master.geometry("600x500")
        master.configure(bg=WHITE)

        # Κεφαλίδα
        title = tk.Label(master, text="GymBuddy", font=FONT_TITLE, fg=BLACK, bg=WHITE)
        title.pack(pady=15)

        # Πλαίσιο Σύνδεσης
        frame = tk.Frame(master, bg=WHITE, bd=2, relief="solid", highlightbackground=BLACK, highlightthickness=2)
        frame.pack(pady=10, padx=30, fill="x")

        # Email
        tk.Label(frame, text="Email", font=FONT_LABEL, bg=WHITE).pack(pady=(10, 0))
        self.email_entry = tk.Entry(frame, font=FONT_ENTRY, relief="solid", bd=1)
        self.email_entry.pack(pady=5, padx=20, ipady=5, fill="x")

        # Password
        tk.Label(frame, text="Κωδικός", font=FONT_LABEL, bg=WHITE).pack(pady=(10, 0))
        self.password_entry = tk.Entry(frame, show="*", font=FONT_ENTRY, relief="solid", bd=1)
        self.password_entry.pack(pady=5, padx=20, ipady=5, fill="x")

        # Login Button
        login_btn = tk.Button(frame, text="Σύνδεση", bg=BLACK, fg=WHITE,
                              font=FONT_LABEL, command=self.login, bd=0, padx=10, pady=5)
        login_btn.pack(pady=15)

        # Κείμενο "Δεν έχεις λογαριασμό;"
        tk.Label(master, text="Δεν έχεις λογαριασμό;", font=FONT_LABEL, bg=WHITE).pack(pady=(10, 0))

        # Register Buttons
        reg_user_btn = tk.Button(master, text="Εγγραφή Χρήστη", bg=PURPLE, fg=WHITE,
                                 font=FONT_LABEL, command=self.open_user_registration, bd=0, padx=10, pady=5)
        reg_user_btn.pack(pady=5)

        reg_trainer_btn = tk.Button(master, text="Εγγραφή Γυμναστή", bg=PURPLE, fg=WHITE,
                                    font=FONT_LABEL, command=self.open_trainer_registration, bd=0, padx=10, pady=5)
        reg_trainer_btn.pack(pady=5)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        messagebox.showinfo("Σύνδεση", f"Προσπάθεια σύνδεσης με {email}")

    def open_user_registration(self):
        RegistrationForm("Χρήστη")

    def open_trainer_registration(self):
        RegistrationForm("Γυμναστή")


class RegistrationForm:
    def __init__(self, role):
        self.window = tk.Toplevel()
        self.window.title(f"Εγγραφή {role}")
        self.window.geometry("400x450")
        self.window.configure(bg=WHITE)

        tk.Label(self.window, text=f"Εγγραφή {role}", font=FONT_TITLE, fg=BLACK, bg=WHITE).pack(pady=15)

        # Όνομα
        self.create_labeled_entry("Όνομα")
        self.name_entry = self.entry

        # Email
        self.create_labeled_entry("Email")
        self.email_entry = self.entry

        # Κωδικός
        self.create_labeled_entry("Κωδικός", show="*")
        self.password_entry = self.entry

        # Περιοχή
        self.create_labeled_entry("Περιοχή")
        self.location_entry = self.entry

        # Κουμπί Εγγραφής
        register_btn = tk.Button(self.window, text="Εγγραφή", bg=PURPLE, fg=WHITE,
                                 font=FONT_LABEL, command=self.register, bd=0, padx=10, pady=5)
        register_btn.pack(pady=20)

    def create_labeled_entry(self, label_text, show=None):
        tk.Label(self.window, text=label_text, font=FONT_LABEL, bg=WHITE).pack()
        self.entry = tk.Entry(self.window, font=FONT_ENTRY, show=show, relief="solid", bd=1)
        self.entry.pack(pady=5, padx=20, ipady=5, fill="x")

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        location = self.location_entry.get()

        messagebox.showinfo("Εγγραφή", f"Εγγραφή επιτυχής για {name} ({email})!")


