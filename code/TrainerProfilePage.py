import tkinter as tk

class TrainerProfilePage(tk.Toplevel):
    MAX_REPORTS = 5

    def __init__(self, trainer_id, db_manager):
        super().__init__()
        self.title("Προφίλ Γυμναστή")
        self.geometry("300x200")
        self.db = db_manager
        self.trainer_id = trainer_id

        tk.Label(self, text=f"Προφίλ Γυμναστή: {trainer_id}").pack(pady=10)

        tk.Button(self, text="Αναφορά", command=lambda: self.reportButtonOnPress("U001")).pack(pady=10)

    def reportButtonOnPress(self, user_id):
        ReportPage(self.trainer_id, user_id, self.db)

    def display(self, user_id):
        ReportPage(self.trainer_id, user_id, self.db)


class ReportPage(tk.Toplevel):
    def __init__(self, trainer_id, user_id, db):
        super().__init__()
        self.trainer_id = trainer_id
        self.user_id = user_id
        self.db = db

        self.title("Σελίδα Αναφοράς Γυμναστή")
        self.geometry("300x300")

        tk.Label(self, text=f"Αναφορά Γυμναστή: {trainer_id}").pack()
        tk.Label(self, text="Παρακαλώ επιλέξτε τον λόγο αναφοράς:").pack(pady=10)

        self.reasons = ["Ακατάλληλη συμπεριφορά", "Ανακριβείς πληροφορίες", "Άλλο"]
        self.reason_var = tk.StringVar(value=self.reasons[0])

        for reason in self.reasons:
            tk.Radiobutton(self, text=reason, variable=self.reason_var, value=reason).pack(anchor=tk.W)

        tk.Label(self, text="Σχόλια:").pack(pady=5)
        self.comment_entry = tk.Entry(self, width=40)
        self.comment_entry.pack()

        tk.Button(self, text="Υποβολή Αναφοράς", command=self.saveReport).pack(pady=10)

    def saveReport(self):
        self.db.saveReport()
        self.destroy()

    def userBanRequest(self):
        print(f"🚫 Too many reports on trainer {self.trainer_id}. Initiating ban review...")

    @staticmethod
    def showSuccessMessage():
        print("✅ Report submitted successfully!")

    @staticmethod
    def showFailMessage():
        print("❌ You have already reported this trainer.")

    @staticmethod
    def redirect():
        print("🔄 Redirecting to homepage...")

    @staticmethod
    def closeMessage():
        print("🗙 Closing message...")
