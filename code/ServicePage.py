
import tkinter as tk
from tkinter import messagebox
from DBManager import DBManager  # Assuming DBManager is a module for database operations


class ServicePage(tk.Toplevel):
    def __init__(self, service_name, trainer_id=None, identity=None, cert=None):
        super().__init__()
        self.title("Προβολή Υπηρεσίας")
        self.geometry("300x200")

        tk.Label(self, text=f"Λεπτομέρειες για την υπηρεσία:").pack(pady=10)
        tk.Label(self, text=service_name, font=("Helvetica", 14, "bold")).pack(pady=5)
        tk.Label(self, text=f"H υπηρεσία {service_name} προσφέρεται από τον γυμναστή: {trainer_id}").pack(pady=5)
        tk.Button(self, text="Προφίλ Γυμναστή", command=lambda: self.open_trainer_profile(trainer_id, DBManager)).pack(pady=10)

        tk.Button(self, text="Κράτηση", command=self.check_time_slot).pack()

        tk.Button(self, text="Κλείσιμο", command=self.destroy).pack(pady=10)

    def check_time_slot(self):
        available = DBManager.check_time_slot()  # Dummy function for now
        if available:
            self.redirect_to_verification()
        else:
            messagebox.showerror("Σφάλμα", "Η ώρα δεν είναι διαθέσιμη.")

    def redirect_to_verification(self):
        self.destroy()
        VerifyPage()  # Go to payment verification

    def open_trainer_profile(self, trainer_id, dbmanager):
        from TrainerProfilePage import TrainerProfilePage
        TrainerProfilePage(trainer_id, dbmanager)  # Open trainer profile page

class VerifyPage(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Επιβεβαίωση και Πληρωμή")
        self.geometry("300x200")

        tk.Button(self, text="Πληρωμή Online", command=self.online_payment).pack()
        tk.Button(self, text="Πληρωμή με Μετρητά", command=self.cash_payment).pack()

    def online_payment(self):
        response = PaymentGateway.process()
        if response == "success":
            DBManager.save_application()
            messagebox.showinfo("Επιτυχία", "Η πληρωμή ολοκληρώθηκε.")
        else:
            messagebox.showerror("Αποτυχία", "Η πληρωμή απέτυχε.")
        self.destroy()


    def cash_payment(self):
        DBManager.save_application()
        messagebox.showinfo("Επιτυχία", "Η αίτηση καταχωρήθηκε. Πληρωμή με μετρητά.")

class PaymentGateway:
    @staticmethod
    def process():
        # Simulate online payment
        print("[DEBUG] Processing online payment...")
        messagebox.showinfo("Πληρωμή", "Η πληρωμή επεξεργάζεται... στο σημειό αυτό μεταβαίνουμε σε μια εξωτερική υπηρεσία πληρωμών (Stripe).")
        return "success"  # or "fail"