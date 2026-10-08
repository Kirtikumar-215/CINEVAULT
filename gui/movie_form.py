import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

from config import GENRES, LANGUAGES, STATUSES
from modules.validation import validate_movie_data

class MovieForm(tk.Toplevel):
    def __init__(self, parent, on_save, movie=None):
        super().__init__(parent)
        self.on_save = on_save
        self.movie = movie
        self.title("Add Movie" if movie is None else "Edit Movie")
        self.geometry("540x760")
        self.minsize(540, 700)
        self.resizable(False, True)
        self.configure(bg="#101827")
        self.transient(parent)
        self.grab_set()

        self.vars = {}
        fields = [
            ("Movie Title", "title", ""),
            ("Rating (0-5)", "rating", ""),
            ("Release Year", "year", ""),
            ("Duration (min)", "duration", ""),
            ("Notes", "notes", ""),
        ]

        container = tk.Frame(self, bg="#101827")
        container.pack(fill="both", expand=True, padx=28, pady=22)

        tk.Label(container, text=self.title(), bg="#101827", fg="white",
                 font=("Segoe UI", 20, "bold")).pack(anchor="w", pady=(0, 18))

        for label, key, default in fields:
            tk.Label(container, text=label, bg="#101827", fg="#aab8cf",
                     font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(8, 4))
            var = tk.StringVar(value=str(movie.get(key, default)) if movie else default)
            self.vars[key] = var
            if key == "notes":
                widget = tk.Entry(container, textvariable=var, bg="#182337", fg="white",
                                  insertbackground="white", relief="flat")
            else:
                widget = tk.Entry(container, textvariable=var, bg="#182337", fg="white",
                                  insertbackground="white", relief="flat")
            widget.pack(fill="x", ipady=9)

        for label, key, values in [
            ("Genre", "genre", GENRES),
            ("Language", "language", LANGUAGES),
            ("Status", "status", STATUSES),
            ("Favorite", "favorite", ["Yes", "No"]),
        ]:
            tk.Label(container, text=label, bg="#101827", fg="#aab8cf",
                     font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(10, 4))
            var = tk.StringVar(value=str(movie.get(key, values[0])) if movie else values[0])
            self.vars[key] = var
            combo = ttk.Combobox(container, textvariable=var, values=values, state="readonly")
            combo.pack(fill="x")

        buttons = tk.Frame(container, bg="#101827")
        buttons.pack(fill="x", pady=22)
        tk.Button(buttons, text="Cancel", command=self.destroy, bg="#26344d", fg="white",
                  relief="flat", padx=18, pady=8).pack(side="right", padx=(8, 0))
        tk.Button(
            buttons,
            text="Add Movie" if movie is None else "Save Changes",
            command=self.save,
            bg="#6c63ff",
            fg="white",
                  relief="flat", padx=18, pady=8).pack(side="right")

    def save(self):
        data = {key: var.get() for key, var in self.vars.items()}
        data["date_added"] = self.movie.get("date_added", "") if self.movie else str(date.today())
        data["date_watched"] = self.movie.get("date_watched", "") if self.movie else ""
        try:
            clean = validate_movie_data(data)
            if clean["status"] == "Watched" and not clean["date_watched"]:
                clean["date_watched"] = str(date.today())
            self.on_save(clean, self.movie["id"] if self.movie else None)
            self.destroy()
        except ValueError as exc:
            messagebox.showerror("Validation Error", str(exc), parent=self)
