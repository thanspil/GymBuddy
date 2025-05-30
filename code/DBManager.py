# ----------------- DB MANAGER -----------------
class DBManager:
    otp_storage = "0000"
    user_password = "pass"
    reports = {}

    @staticmethod
    def sendResetEmail(email):
        print(f"[DEBUG] Αποστολή email επαναφοράς στο {email} με OTP: {DBManager.otp_storage}")

    @staticmethod
    def checkOTP(otp_input):
        return otp_input == DBManager.otp_storage

    @staticmethod
    def resetUserPass(new_pass):
        DBManager.user_password = new_pass
        print(f"[DEBUG] Password reset to: {new_pass}")

    def checkEmailUnique(self, email):
        if email == "ME":
            print("[DEBUG] Email ME is already used")
            return False

    def checkValCode(self, code):
        return code == "0000"

    def addUser(self, email):
        print(f"Προσθήκη χρήστη: {email}")

    def addTrainer(self, email, identity, cert):
        print(f"Προσθήκη γυμναστή: {email} - ID: {identity}, Πτυχίο: {cert}")

    @staticmethod
    def check_time_slot():
        print("[DEBUG] Checking time slot availability...")
        return True

    @staticmethod
    def save_application():
        print("Application saved to database")

    def checkReportExists(self, trainer_id, user_id):
        return user_id in self.reports.get(trainer_id, [])

    def saveReport():
        print("[DEBUG] Saving report to database")

    def checkReportCount(self, trainer_id):
        return len(self.reports.get(trainer_id, []))
