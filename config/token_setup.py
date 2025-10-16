import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox
from .config import ENV_PATH


def load_token():
    if os.path.exists(ENV_PATH):
        load_dotenv(ENV_PATH)
        return os.getenv("DISCORD_BOT_TOKEN", "")
    return ""

def save_token(token):
    with open(ENV_PATH, "w") as f:
        f.write(f"DISCORD_BOT_TOKEN={token}\n")

def open_token_editor():
    root = tk.Tk()
    root.title("Configuración del Bot de Música")
    root.geometry("400x200")
    root.resizable(False, False)

    tk.Label(root, text="Token del Bot de Discord:", font=("Segoe UI", 10)).pack(pady=10)

    token_var = tk.StringVar(value=load_token())
    entry = tk.Entry(root, textvariable=token_var, width=45, show="*", font=("Segoe UI", 10))
    entry.pack(pady=5)

    def guardar():
        token = token_var.get().strip()
        if not token:
            messagebox.showerror("Error", "El token no puede estar vacío.")
            return
        save_token(token)
        messagebox.showinfo("Éxito", "Token guardado correctamente.")
        root.destroy()

    tk.Button(root, text="Guardar", command=guardar, bg="#4CAF50", fg="white", width=12).pack(pady=15)
    root.mainloop()

