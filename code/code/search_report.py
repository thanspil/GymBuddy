import tkinter as tk
from tkinter import ttk, messagebox

# Δείγμα προφίλ
all_profiles = [
    {"name": "Γιώργος Π.", "price": 40, "location": "Πάτρα"},
    {"name": "Μαρία Α.", "price": 60, "location": "Αθήνα"},
    {"name": "Νίκος Κ.", "price": 30, "location": "Πάτρα"},
    {"name": "Ιωάννα Ν.", "price": 80, "location": "Θεσσαλονίκη"},
    {"name": "Γεωργία Σ.", "price": 55, "location": "Πάτρα"},
    {"name": "Ανδρέας Π.", "price": 35, "location": "Αθήνα"},
    {"name": "Ελένη Μ.", "price": 70, "location": "Πάτρα"},
    {"name": "Χρήστος Λ.", "price": 50, "location": "Θεσσαλονίκη"},
    {"name": "Άννα Τ.", "price": 65, "location": "Αθήνα"},
]

def show_profiles():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    name_query = name_entry.get().lower()
    location_query = location_entry.get().lower()
    try:
        price_min = int(price_min_entry.get())
    except:
        price_min = 0
    try:
        price_max = int(price_max_entry.get())
    except:
        price_max = 999

    filtered = []
    for p in all_profiles:
        if (name_query in p["name"].lower() and
            location_query in p["location"].lower() and
            price_min <= p["price"] <= price_max):
            filtered.append(p)

    if not filtered:
        ttk.Label(scrollable_frame, text="Δεν βρέθηκαν αποτελέσματα.").pack(pady=10)

    for profile in filtered:
        card = ttk.Frame(scrollable_frame, padding=10, relief="raised")
        card.pack(pady=5, padx=10, fill="x")
        ttk.Label(card, text=profile["name"], font=("Arial", 12, "bold")).pack(anchor="w")
        ttk.Label(card, text=f"Περιοχή: {profile['location']} | Τιμή: {profile['price']}€").pack(anchor="w")
        tk.Button(card, text="Προβολή προφίλ", command=lambda p=profile: open_profile(p),
                  bg="black", fg="white", padx=10, pady=5, relief="flat").pack(pady=5)


def open_profile(profile):
    popup = tk.Toplevel(root)
    popup.title("Προφίλ Γυμναστή")
    popup.geometry("700x500")
    popup.configure(bg="white")

    # Εικόνα placeholder
    image_frame = tk.Frame(popup, bg="lightgray", width=200, height=200)
    image_frame.pack(pady=10)
    tk.Label(image_frame, text="[Εικόνα]", bg="lightgray").pack(expand=True)

    # Όνομα και τιμή
    info_frame = tk.Frame(popup, bg="white")
    info_frame.pack(pady=10)

    tk.Label(info_frame, text=profile["name"], font=("Arial", 16, "bold"), bg="white").pack(anchor="w")
    tk.Label(info_frame, text="Crossfit", font=("Arial", 10, "italic"), bg="white", fg="green").pack(anchor="w")
    tk.Label(info_frame, text=f"{profile['price']}€/ώρα", font=("Arial", 14), bg="white").pack(anchor="w", pady=5)

    # About me
    about = tk.LabelFrame(popup, text="About me", bg="white", padx=10, pady=10)
    about.pack(padx=10, pady=10, fill="x")
    tk.Label(about, text="Περιγραφή...",
             wraplength=600, justify="left", bg="white").pack()

    # Add Review Button
    add_review_button = tk.Button(popup, text="Προσθήκη Αξιολόγησης",
                                   bg="purple", fg="white", padx=10, pady=5, relief="flat")

    # Reviews
    review_section = tk.Frame(popup, bg="white")
    review_section.pack(pady=10, fill="x")
    tk.Label(review_section, text="Latest reviews", font=("Arial", 12, "bold"), bg="white").pack(anchor="w", padx=10)

    # Κουμπί Αναφοράς στο τέλος
    report_button = tk.Button(
        popup,
        text="Αναφορά",
        command=lambda: report_profile(profile),
        bg="red",
        fg="white",
        padx=40,
        pady=5,
        relief="flat"
    )
    report_button.pack(pady=10)

    def report_profile(profile):
        report_win = tk.Toplevel(root)
        report_win.title("Αναφορά Χρήστη / Υπηρεσίας")
        report_win.geometry("500x500")
        report_win.configure(bg="white")

        tk.Label(report_win, text="Αναφορά για: " + profile["name"], font=("Arial", 14, "bold"), bg="white").pack(
            pady=10)

        tk.Label(report_win, text="Επέλεξε λόγο αναφοράς:", font=("Arial", 10), bg="white").pack(anchor="w", padx=20)

        reasons = [
            "Ανάρμοστη συμπεριφορά",
            "Ψευδής διαφήμιση",
            "Απρεπής περιγραφή",
            "Σπαμ",
            "Άλλο"
        ]

        reason_var = tk.StringVar()
        for reason in reasons:
            tk.Radiobutton(report_win, text=reason, variable=reason_var, value=reason, bg="white").pack(anchor="w",
                                                                                                        padx=40)

        tk.Label(report_win, text="Περισσότερες λεπτομέρειες (προαιρετικό):", bg="white").pack(pady=10, anchor="w",
                                                                                               padx=20)
        details_entry = tk.Text(report_win, height=5, width=50)
        details_entry.pack(padx=20)

        def submit_report():
            selected = reason_var.get()
            details = details_entry.get("1.0", "end").strip()

            if not selected:
                messagebox.showwarning("Προσοχή", "Παρακαλώ επίλεξε λόγο αναφοράς.")
                return

            # TODO BACKEND anaφορά προφίλ.
            print(f"Αναφέρθηκε ο {profile['name']} για: {selected}. Λεπτομέρειες: {details}")
            messagebox.showinfo("Υποβλήθηκε", "Η αναφορά σου καταγράφηκε.")
            report_win.destroy()

        tk.Button(report_win, text="Υποβολή Αναφοράς", command=submit_report, bg="black", fg="white", padx=20,
                  pady=5).pack(pady=20)


# === GUI ===

root = tk.Tk()
root.title("GymBuddy")
root.geometry("900x600")
root.configure(bg="white")

# Τίτλος
title_frame = ttk.Frame(root)
title_frame.pack(pady=10)
ttk.Label(title_frame, text="GymBuddy", font=("Arial", 22, "bold")).pack()
ttk.Label(title_frame, text="Κάνε την αναζήτησή σου και βρες αυτό που σου ταιριάζει!",
          font=("Arial", 12)).pack()

# Κύριο πλαίσιο
main_frame = tk.Frame(root, bg="white")
main_frame.pack(fill="both", expand=True)

# Φίλτρα (αριστερά)
filter_frame = tk.Frame(main_frame, bg="white", padx=20)
filter_frame.pack(side="left", fill="y", pady=10)

tk.Label(filter_frame, text="Αναζήτηση ονόματος:", bg="white").pack(anchor="w")
name_entry = tk.Entry(filter_frame, width=25)
name_entry.pack(pady=5)

tk.Label(filter_frame, text="Περιοχή:", bg="white").pack(anchor="w")
location_entry = tk.Entry(filter_frame, width=25)
location_entry.insert(0, "")
location_entry.pack(pady=5)

tk.Label(filter_frame, text="Εύρος τιμής (€):", bg="white").pack(anchor="w")
price_range_frame = tk.Frame(filter_frame, bg="white")
price_range_frame.pack(pady=5)

price_min_entry = tk.Entry(price_range_frame, width=8)
price_min_entry.insert(0, "0")
price_min_entry.pack(side="left", padx=5)

price_max_entry = tk.Entry(price_range_frame, width=8)
price_max_entry.insert(0, "999")
price_max_entry.pack(side="left", padx=5)

# ΜΕΓΑΛΟ, ΜΑΥΡΟ ΚΟΥΜΠΙ
def style_search_button(button):
    button.configure(
        background="black",
        foreground="white",
        font=("Arial", 11, "bold"),
        borderwidth=0,
        relief="flat",
        padx=10,
        pady=10
    )
    button.bind("<Enter>", lambda e: button.configure(background="#333"))
    button.bind("<Leave>", lambda e: button.configure(background="black"))

search_button = tk.Button(filter_frame, text="Αναζήτηση", command=show_profiles)
style_search_button(search_button)
search_button.pack(pady=40, fill="x")
""
# Πλαίσιο προφίλ με Scrollbar
profile_container = tk.Frame(main_frame, bg="white")
profile_container.pack(side="left", fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(profile_container, bg="white", highlightthickness=0)
scrollbar = ttk.Scrollbar(profile_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="white")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Εμφάνιση όλων στην αρχή
show_profiles()

root.mainloop()
