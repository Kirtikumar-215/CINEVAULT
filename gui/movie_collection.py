import tkinter as tk
from tkinter import ttk, messagebox

from config import GENRES, LANGUAGES, STATUSES
from gui.movie_form import MovieForm
from gui.widgets import style_tree

class MovieCollectionView(tk.Frame):
    def __init__(self, parent, manager, on_change=None):
        super().__init__(parent, bg="#0f1725")
        self.manager = manager
        self.on_change = on_change
        self.search_var = tk.StringVar()
        self.genre_var = tk.StringVar(value="All")
        self.status_var = tk.StringVar(value="All")
        self.language_var = tk.StringVar(value="All")
        self.favorite_var = tk.StringVar(value="All")
        self.build()
        self.refresh()

    def build(self):
        top = tk.Frame(self, bg="#0f1725")
        top.pack(fill="x", padx=24, pady=(24, 12))
        tk.Label(top, text="Movie Collection", bg="#0f1725", fg="white",
                 font=("Segoe UI", 22, "bold")).pack(side="left")
        tk.Button(top, text="+ Add Movie", command=self.add_movie, bg="#6c63ff",
                  fg="white", relief="flat", padx=16, pady=8).pack(side="right")

        controls = tk.Frame(self, bg="#172033")
        controls.pack(fill="x", padx=24, pady=8)
        tk.Label(controls, text="Search", bg="#172033", fg="#9eb0cb").pack(side="left", padx=(12, 4))
        search = tk.Entry(controls, textvariable=self.search_var, bg="#0f1725", fg="white",
                          insertbackground="white", relief="flat", width=25)
        search.pack(side="left", ipady=7)
        search.bind("<KeyRelease>", lambda e: self.refresh())

        for label, var, values in [
            ("Genre", self.genre_var, ["All"] + GENRES),
            ("Status", self.status_var, ["All"] + STATUSES),
            ("Language", self.language_var, ["All"] + LANGUAGES),
            ("Favorite", self.favorite_var, ["All", "Yes", "No"]),
        ]:
            tk.Label(controls, text=label, bg="#172033", fg="#9eb0cb").pack(side="left", padx=(12, 4))
            combo = ttk.Combobox(controls, textvariable=var, values=values, state="readonly", width=13)
            combo.pack(side="left")
            combo.bind("<<ComboboxSelected>>", lambda e: self.refresh())

        table_frame = tk.Frame(self, bg="#0f1725")
        table_frame.pack(fill="both", expand=True, padx=24, pady=12)
        columns = ("id", "title", "genre", "rating", "year", "language", "status", "favorite")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        headings = {
            "id": "ID", "title": "Movie", "genre": "Genre", "rating": "Rating",
            "year": "Year", "language": "Language", "status": "Status", "favorite": "★"
        }
        widths = {"id": 45, "title": 190, "genre": 100, "rating": 70, "year": 70,
                  "language": 95, "status": 115, "favorite": 45}
        for col in columns:
            self.tree.heading(col, text=headings[col])
            self.tree.column(col, width=widths[col], anchor="center")
        self.tree.column("title", anchor="w")
        style_tree(self.tree)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        actions = tk.Frame(self, bg="#0f1725")
        actions.pack(fill="x", padx=24, pady=(0, 20))
        tk.Button(actions, text="Edit Selected", command=self.edit_movie, bg="#26344d",
                  fg="white", relief="flat", padx=14, pady=8).pack(side="left", padx=(0, 8))
        tk.Button(actions, text="Delete Selected", command=self.delete_movie, bg="#b83b5e",
                  fg="white", relief="flat", padx=14, pady=8).pack(side="left")

    def refresh(self):
        if not hasattr(self, "tree"):
            return
        df = self.manager.search_movies(self.search_var.get())
        for column, variable in (
            ("genre", self.genre_var),
            ("status", self.status_var),
            ("language", self.language_var),
            ("favorite", self.favorite_var),
        ):
            value = variable.get()
            if value != "All":
                df = df[df[column] == value]
        for item in self.tree.get_children():
            self.tree.delete(item)
        for _, row in df.iterrows():
            values = tuple(row[c] for c in ("id", "title", "genre", "rating", "year", "language", "status", "favorite"))
            tags = ("favorite",) if row["favorite"] == "Yes" else ()
            self.tree.insert("", "end", values=values, tags=tags)

    def selected_id(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Select Movie", "Please select a movie first.", parent=self)
            return None
        return int(self.tree.item(selection[0], "values")[0])

    def add_movie(self):
        MovieForm(self, self.save_movie)

    def edit_movie(self):
        movie_id = self.selected_id()
        if movie_id is not None:
            MovieForm(self, self.save_movie, self.manager.get_movie(movie_id))

    def save_movie(self, data, movie_id=None):
        try:
            if movie_id is None:
                self.manager.add_movie(data)
            else:
                self.manager.update_movie(movie_id, data)
            self.refresh()
            if self.on_change:
                self.on_change()
        except ValueError as exc:
            messagebox.showerror("Error", str(exc), parent=self)

    def delete_movie(self):
        movie_id = self.selected_id()
        if movie_id is not None and messagebox.askyesno(
            "Confirm Delete", "Delete the selected movie?", parent=self
        ):
            try:
                self.manager.delete_movie(movie_id)
                self.refresh()
                if self.on_change:
                    self.on_change()
            except ValueError as exc:
                messagebox.showerror("Error", str(exc), parent=self)
