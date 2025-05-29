
import tkinter as tk
from tkinter import ttk, messagebox

class CreatePersonalProgramWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Δημιουργία Εξατομικευμένου Προγράμματος")
        self.master.geometry("500x500")
        self.master.configure(bg="#f0f0f0")

        self.customers = ["Γιώργος Παπαδόπουλος", "Μαρία Κωνσταντίνου"]
        self.create_form()

    def create_form(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="white")
        style.configure("TLabel", background="white", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), background="white", foreground="#333")
        style.configure("TButton", padding=6, relief="flat", background="#333", foreground="white")

        card = ttk.Frame(self.master, padding=20, style="TFrame")
        card.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(card, text="Νέο Εξατομικευμένο Πρόγραμμα", style="Header.TLabel").pack(pady=(0, 20))

        ttk.Label(card, text="Επιλογή Πελάτη:").pack(anchor="w")
        self.customer_var = tk.StringVar(value=self.customers[0])
        ttk.Combobox(card, textvariable=self.customer_var, values=self.customers).pack(pady=(0, 10))

        self.title_entry = self.add_field(card, "Τίτλος Προγράμματος:")

        ttk.Label(card, text="Λεπτομέρειες:").pack(anchor="w")
        self.details_text = tk.Text(card, height=6, relief="solid", bd=1)
        self.details_text.pack(fill="both", pady=(0, 10))

        ttk.Button(card, text="Δημιουργία", command=self.save_program).pack()

    def add_field(self, parent, label_text):
        ttk.Label(parent, text=label_text).pack(anchor="w")
        entry = ttk.Entry(parent, width=40)
        entry.pack(pady=(0, 10))
        return entry

    def save_program(self):
        customer = self.customer_var.get()
        title = self.title_entry.get()
        details = self.details_text.get("1.0", "end").strip()

        if not customer or not title:
            messagebox.showerror("Σφάλμα", "Όλα τα πεδία είναι υποχρεωτικά.")
            return

        messagebox.showinfo("Επιτυχία", f"Το πρόγραμμα για τον/την {customer} αποθηκεύτηκε.")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CreatePersonalProgramWindow(root)
    root.mainloop()
