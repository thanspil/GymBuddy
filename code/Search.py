import tkinter as tk
from tkinter import messagebox
from ServicePage import ServicePage
from Profile import ProfilePage

# Mock functions
def get_user_history():
    return ["Pilates", "Yoga", "Strength Training"]

def get_user_location():
    return "Athens"

def search_services(location):
    return ["Yoga Studio", "Gym", "Trainer"] if location == "Athens" else []


class ResultsScreen(tk.Toplevel):
    def __init__(self, results):
        super().__init__()
        self.title("Αποτελέσματα")
        self.geometry("300x300")
        # your location
        tk.Label(self, text="Αποτελέσματα για την τοποθεσία σας:").pack(pady=10)
        tk.Label(self, text=get_user_location()).pack(pady=5)
        tk.Label(self, text="Βρέθηκαν τα εξής:").pack(pady=10)

        for result in results:
            frame = tk.Frame(self)
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=result).pack(side="left", padx=5)
            tk.Button(frame, text="Προβολή", command=lambda r=result: self.view_service(r)).pack(side="right", padx=5)

    def view_service(self, service_name):
        ServicePage(service_name, trainer_id="123", identity="Trainer ID", cert="Certification Info")


class SearchHistoryScreen(tk.Tk):
    def __init__(self, history):
        super().__init__()
        self.title("Ιστορικό Αναζητήσεων")
        self.geometry("400x300")

        # Search bar
        self.search_bar = tk.Entry(self, width=30)
        self.search_bar.pack(pady=10)

        # Search history
        tk.Label(self, text="Προηγούμενες αναζητήσεις:").pack()
        for item in history:
            tk.Label(self, text=item).pack()

        # Search button
        tk.Button(self, text="Αναζήτηση", command=self.search_button_on_click).pack(pady=10)
        # Back button
        tk.Button(self, text="Πίσω", command=self.go_back).pack(pady=20)

    def go_back(self):
        self.destroy()  # Κλείσε αυτό το παράθυρο
        ProfilePage()  # Επιστροφή στην αρχική σελίδα προφίλ

    def search_button_on_click(self):
        location = get_user_location()
        results = search_services(location)

        if results:
            ResultsScreen(results)
        else:
            messagebox.showinfo("Αποτελέσματα", "Δεν βρέθηκαν αποτελέσματα.")


class SearchScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Αναζήτηση")
        self.geometry("400x300")

        self.search_bar = tk.Entry(self, width=30)
        self.search_bar.pack(pady=20)

        self.search_bar.bind("<Button-1>", self.search_bar_on_click)

        tk.Button(self, text="Αναζήτηση", command=self.search_button_on_click).pack(pady=10)

        tk.Button(self, text="Προφίλ Χρήστη", command=lambda: ProfilePage()).pack(pady=10)



    def search_bar_on_click(self, event=None):
        history = get_user_history()
        self.after(10, lambda: [self.destroy(), SearchHistoryScreen(history)])

    def search_button_on_click(self):
        location = get_user_location()
        results = search_services(location)

        if results:
            ResultsScreen(results)
        else:
            messagebox.showinfo("Αποτελέσματα", "Δεν βρέθηκαν αποτελέσματα.")




if __name__ == "__main__":
    app = SearchScreen()
    app.mainloop()
