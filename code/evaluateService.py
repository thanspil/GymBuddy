
import tkinter as tk
from tkinter import ttk, messagebox

class EvaluateServiceWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Αξιολόγηση Υπηρεσίας")
        self.master.geometry("500x500")
        self.master.configure(bg="#f0f0f0")

        self.services = ["Personal Training", "Group Yoga", "Pilates Online"]
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

        ttk.Label(card, text="Αξιολόγηση Υπηρεσίας", style="Header.TLabel").pack(pady=(0, 20))

        ttk.Label(card, text="Επιλογή Υπηρεσίας:").pack(anchor="w")
        self.service_var = tk.StringVar(value=self.services[0])
        ttk.Combobox(card, textvariable=self.service_var, values=self.services).pack(pady=(0, 10))

        ttk.Label(card, text="Βαθμολογία (1-5):").pack(anchor="w")
        self.rating_var = tk.StringVar(value="5")
        ttk.Combobox(card, textvariable=self.rating_var, values=["1", "2", "3", "4", "5"]).pack(pady=(0, 10))

        ttk.Label(card, text="Σχόλια:").pack(anchor="w")
        self.comments_text = tk.Text(card, height=6, relief="solid", bd=1)
        self.comments_text.pack(fill="both", pady=(0, 10))

        ttk.Button(card, text="Υποβολή Αξιολόγησης", command=self.submit_evaluation).pack()

    def submit_evaluation(self):
        service = self.service_var.get()
        rating = self.rating_var.get()
        comments = self.comments_text.get("1.0", "end").strip()

        if not service or not rating:
            messagebox.showerror("Σφάλμα", "Όλα τα πεδία είναι υποχρεωτικά.")
            return

        print(f"Αξιολόγηση: {service}, Βαθμολογία: {rating}, Σχόλια: {comments}")
        messagebox.showinfo("Επιτυχία", "Η αξιολόγηση καταχωρήθηκε.")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EvaluateServiceWindow(root)
    root.mainloop()
