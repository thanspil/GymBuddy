
import tkinter as tk
from tkinter import ttk, messagebox

class CreateServiceWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Δημιουργία Υπηρεσίας")
        self.master.geometry("500x450")
        self.master.configure(bg="#f0f0f0")

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

        ttk.Label(card, text="Δημιουργία Υπηρεσίας", style="Header.TLabel").pack(pady=(0, 20))

        self.name_entry = self.add_field(card, "Όνομα Υπηρεσίας:")
        self.price_entry = self.add_field(card, "Τιμή (€):")
        self.capacity_entry = self.add_field(card, "Μέγιστος Αριθμός Ατόμων:")

        ttk.Label(card, text="Τύπος Υπηρεσίας:").pack(anchor="w")
        self.service_type = ttk.Combobox(card, values=["Δια-ζώσης", "Διαδικτυακή", "Εξατομικευμένο"])
        self.service_type.pack(pady=(0, 20))

        ttk.Button(card, text="Προσθήκη", command=self.add_service).pack()

    def add_field(self, parent, label_text):
        ttk.Label(parent, text=label_text).pack(anchor="w")
        entry = ttk.Entry(parent, width=40)
        entry.pack(pady=(0, 10))
        return entry

    def add_service(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Σφάλμα", "Το όνομα της υπηρεσίας είναι απαραίτητο.")
            return

        messagebox.showinfo("Επιτυχία", f"Η υπηρεσία '{name}' προστέθηκε.")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateServiceWindow(root)
    root.mainloop()
