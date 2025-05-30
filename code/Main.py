# Main.py

from LoginAndReg import LoginScreen

if __name__ == "__main__":
    print("[DEBUG] To enter profile page:")
    print(f"[DEBUG] Use username:user and password:pass to login as user.")
    print(f"[DEBUG] Use username:trainer and password:pass to login as trainer.")
    print(f"[DEBUG] Username:ME and password:pass is already used")
    LoginScreen().mainloop()

