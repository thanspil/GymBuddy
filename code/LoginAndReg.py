import tkinter as tk
from tkinter import messagebox, filedialog

from DBManager import DBManager
from Profile import ProfilePage, ProfilePageAsTrainer

# ----------------- LOGIN SCREEN -----------------
class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        tk.Label(self, text="Οθόνη Σύνδεσης", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Όνομα Χρήστη:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Κωδικός:").pack()
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()

        tk.Button(self, text="Σύνδεση", command=self.login).pack(pady=(10, 5))
        tk.Button(self, text="Ξέχασα τον κωδικό μου", command=self.passResetButtonOnPress).pack()

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Εγγραφή Χρήστη", command=self.registerUser).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Εγγραφή Γυμναστή", command=self.registerTrainer).pack(side="left")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"[DEBUG] Προσπάθεια σύνδεσης με {username} / {password}")
        #open profile page
        if username == "user" and password == "pass":
            self.destroy()
            ProfilePage(email=username).mainloop()
        elif username == "trainer" and password == "pass":
            self.destroy()
            ProfilePageAsTrainer(email=username, identity="123456789", cert="Πτυχίο Γυμναστικής").mainloop()
        elif username == "ME" and password == "pass":
            EmailInUseMessage().showMessage()
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.username_entry.focus()
        else:
            messagebox.showerror("Σφάλμα", "Λάθος όνομα χρήστη ή κωδικός.")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.username_entry.focus()

    def passResetButtonOnPress(self):
        self.destroy()
        PassResetPage().mainloop()

    def registerUser(self):
        self.destroy()
        RegistrationScreenTrainee().mainloop()

    def registerTrainer(self):
        self.destroy()
        RegistrationScreenTrainer().mainloop()

# ----------------- REGISTRATION SCREEN -----------------
class RegistrationScreenTrainee(tk.Tk):
    def __init__(self):
        super().__init__()
        tk.Label(self, text="Εγγραφή Χρήστη", font=("Arial", 16)).pack(pady=10)

        tk.Label(self, text="Email:").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()
        tk.Label(self, text="Ονοματεπώνυμο:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()
        tk.Label(self, text="Κωδικός:").pack()
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack()

        tk.Button(self, text="Αποστολή", command=self.sendButtonOnPress).pack()

    def sendButtonOnPress(self):
        email = self.email_entry.get()
        name = self.name_entry.get()
        password = self.password_entry.get()

        db = DBManager()
        if not db.checkEmailUnique(email):
            EmailInUseMessage().showMessage()
            return

        if not self.checkRegFields(email, name, password):
            WrongInfoMessage().showMessage()
            return

        self.sendCodeEmail(email)
        self.destroy()
        ValidationScreen(email).mainloop()

    def checkRegFields(self, email, name, password):
        return bool(email.strip()) and bool(name.strip()) and bool(password.strip())

    def sendCodeEmail(self, email):

        print(f"Αποστολή email επιβεβαίωσης στο {email} με κωδικό επιβεβαιωσης OTP 0000")

# ----------------- REGISTRATION SCREEN FOR TRAINER -----------------
class RegistrationScreenTrainer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Εγγραφή Γυμναστή")

        tk.Label(self, text="Εγγραφή Γυμναστή", font=("Arial", 16)).pack(pady=10)

        self.email_entry = self.createLabeledEntry("Email:")
        self.name_entry = self.createLabeledEntry("Ονοματεπώνυμο:")
        self.password_entry = self.createLabeledEntry("Κωδικός:", show="*")
        self.id_entry = self.createLabeledEntry("Αριθμός Ταυτότητας:")
        self.certificate_entry = self.createLabeledEntry("Πτυχίο/Πιστοποίηση:")

        tk.Button(self, text="Επόμενο", command=self.nextStep).pack(pady=10)


    def createLabeledEntry(self, label, show=None):
        tk.Label(self, text=label).pack()
        entry = tk.Entry(self, show=show) if show else tk.Entry(self)
        entry.pack()
        return entry

    def nextStep(self):
        email = self.email_entry.get()
        name = self.name_entry.get()
        password = self.password_entry.get()
        identity = self.id_entry.get()
        cert = self.certificate_entry.get()

        if not all([email.strip(), name.strip(), password.strip(), identity.strip(), cert.strip()]):
            WrongInfoMessage().showMessage()
            messagebox.showwarning("Σφάλμα", "Παρακαλώ συμπληρώστε όλα τα πεδία.")
            return

        db = DBManager()
        if not db.checkEmailUnique(email):
            EmailInUseMessage().showMessage()
            messagebox.showwarning("Σφάλμα", "Το email χρησιμοποιείται ήδη από άλλον χρήστη.")
            return

        self.destroy()
        BankInfoScreen(email, name, password, identity, cert).mainloop()

    def sendCodeEmail(self, email):
        print(f"Αποστολή email επιβεβαίωσης στο {email} με κωδικό...")

# ----------------- STEP 2: BANK INFO -----------------
class BankInfoScreen(tk.Tk):
    def __init__(self, email, name, password, identity, cert):
        super().__init__()
        self.title("Τραπεζικά Στοιχεία")
        self.data = {
            "email": email,
            "name": name,
            "password": password,
            "identity": identity,
            "certificate": cert
        }


        tk.Label(self, text="Τραπεζικά Στοιχεία", font=("Arial", 16)).pack(pady=10)
        self.iban_entry = self.createLabeledEntry("IBAN:")

        tk.Button(self, text="Επόμενο", command=self.nextStep).pack(pady=10)

    def createLabeledEntry(self, label):
        tk.Label(self, text=label).pack()
        entry = tk.Entry(self)
        entry.pack()
        return entry

    def nextStep(self):
        iban = self.iban_entry.get()
        if not iban.strip():
            WrongInfoMessage().showMessage()
            return

        self.data["iban"] = iban
        self.destroy()
        DocumentUploadScreen(self.data).mainloop()

# ----------------- STEP 3: DOCUMENT UPLOAD -----------------
class DocumentUploadScreen(tk.Tk):
    def __init__(self, data):
        super().__init__()
        self.title("Ανέβασμα Εγγράφων")
        self.data = data
        self.id_file = None
        self.cert_file = None

        tk.Label(self, text="Ανέβασε Ταυτότητα (PDF):").pack()
        tk.Button(self, text="Επιλογή Αρχείου", command=self.selectID).pack()
        self.id_label = tk.Label(self, text="Κανένα αρχείο επιλεγμένο")
        self.id_label.pack()

        tk.Label(self, text="Ανέβασε Άδεια Επαγγέλματος (PDF):").pack()
        tk.Button(self, text="Επιλογή Αρχείου", command=self.selectCert).pack()
        self.cert_label = tk.Label(self, text="Κανένα αρχείο επιλεγμένο")
        self.cert_label.pack()

        tk.Button(self, text="Αποθήκευση & Σύνδεση", command=self.saveAndFinish).pack(pady=10)

    def selectID(self):
        path = filedialog.askopenfilename(filetypes=[("PDF αρχεία", "*.pdf")])
        if path:
            self.id_file = path
            self.id_label.config(text=path.split("/")[-1])

    def selectCert(self):
        path = filedialog.askopenfilename(filetypes=[("PDF αρχεία", "*.pdf")])
        if path:
            self.cert_file = path
            self.cert_label.config(text=path.split("/")[-1])

    def saveAndFinish(self):
        if not self.id_file or not self.cert_file:
            messagebox.showwarning("Απαιτούνται αρχεία", "Πρέπει να ανεβάσεις και τα δύο PDF.")
            return

        db = DBManager()
        db.addTrainer(
            self.data["email"],
            self.id_file,
            self.cert_file
        )

        self.destroy()
        ProfilePageAsTrainer(email=self.data["email"], identity=self.data["identity"], cert=self.data["certificate"])


# ----------------- VALIDATION SCREEN -----------------
class ValidationScreen(tk.Tk):
    def __init__(self, email):
        super().__init__()
        self.email = email
        tk.Label(self, text="Επιβεβαίωση Email").pack(pady=10)

        self.code_entry = tk.Entry(self)
        self.code_entry.pack()

        tk.Button(self, text="Επιβεβαίωση", command=self.sendCodeValidation).pack()
        tk.Button(self, text="Επαναποστολή", command=self.resendCodeButtonOnPress).pack()

    def sendCodeValidation(self):
        code = self.code_entry.get()
        db = DBManager()

        if db.checkValCode(code):
            print("Ο κωδικός επιβεβαίωσης είναι σωστός.")
            db.addUser(self.email)
            self.destroy()
            ProfilePage(email=self.email).mainloop()
        else:
            WrongCodeMessage().showMessage()

    def resendCodeButtonOnPress(self):
        RegistrationScreenTrainee().sendCodeEmail(self.email)

# ----------------- PASSWORD RESET -----------------
class PassResetPage(tk.Tk):
    def __init__(self):
        super().__init__()
        tk.Label(self, text="Επαναφορά Κωδικού: εισάγετε το email για ποστολή κωδικού OTP.").pack(pady=10)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()
        tk.Button(self, text="Αποστολή", command=self.resetButtonOnPress).pack()

    def resetButtonOnPress(self):
        email = self.email_entry.get()
        DBManager.sendResetEmail(email)
        self.destroy()
        OTPPage().mainloop()

class OTPPage(tk.Tk):
    def __init__(self):
        super().__init__()
        tk.Label(self, text="Εισαγωγή OTP και νέου κωδικού").pack(pady=10)
        print("[DEBUG] OTP code is 0000")

        tk.Label(self, text="Κωδικός OTP:").pack()
        self.otp_entry = tk.Entry(self)
        self.otp_entry.pack()
        tk.Label(self, text="Νέo Password:").pack()
        self.new_pass_entry = tk.Entry(self, show='*')
        self.new_pass_entry.pack()

        tk.Button(self, text="Επιβεβαίωση", command=self.resetButtonOnPress).pack()

    def resetButtonOnPress(self):
        otp = self.otp_entry.get()
        new_pass = self.new_pass_entry.get()

        if DBManager.checkOTP(otp):
            DBManager.resetUserPass(new_pass)
            messagebox.showinfo("Success", "Ο κωδικός επαναφέρθηκε.")
            self.destroy()
            LoginScreen().mainloop()
        else:
            messagebox.showerror("Σφάλμα", "Λάθος κωδικός OTP: παρακαλώ προσπαθήστε ξανά αργότερα.")
            self.destroy()
            LoginScreen().mainloop()

# ----------------- HELPERS -----------------

class EmailInUseMessage:
    def showMessage(self):
        messagebox.showwarning("Σφάλμα", "Το email χρησιμοποιείται ήδη από άλλον χρήστη.")



class WrongInfoMessage:
    def showMessage(self):
        print("⚠️ Παρακαλώ συμπληρώστε σωστά όλα τα πεδία.")
        messagebox.showwarning("Σφάλμα", "Παρακαλώ συμπληρώστε σωστά όλα τα πεδία.")

class WrongCodeMessage:
    def showMessage(self):
        print("⚠️ Ο κωδικός επιβεβαίωσης είναι λάθος.")
        messagebox.showerror("Σφάλμα", "Ο κωδικός επιβεβαίωσης είναι λάθος. Παρακαλώ προσπαθήστε ξανά.")
