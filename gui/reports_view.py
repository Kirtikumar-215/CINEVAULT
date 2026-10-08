import tkinter as tk
from tkinter import messagebox
from charts.genre_chart import genre_chart
from charts.status_chart import status_chart
from charts.rating_chart import rating_chart
from charts.yearly_chart import yearly_chart

class ReportsView(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent, bg="#0f1725")
        self.manager = manager
        self.build()

    def build(self):
        tk.Label(self, text="Visual Reports", bg="#0f1725", fg="white",
                 font=("Segoe UI", 25, "bold")).pack(anchor="w", padx=28, pady=(26, 5))
        tk.Label(self, text="Four meaningful Matplotlib reports generated from your collection.",
                 bg="#0f1725", fg="#7185a5", font=("Segoe UI", 10)).pack(anchor="w", padx=28, pady=(0, 20))
        grid = tk.Frame(self, bg="#0f1725")
        grid.pack(fill="both", expand=True, padx=28)
        buttons = [
            ("Genre Distribution", genre_chart),
            ("Viewing Status", status_chart),
            ("Rating Distribution", rating_chart),
            ("Yearly Viewing Trend", yearly_chart),
        ]
        for i, (label, func) in enumerate(buttons):
            card = tk.Frame(grid, bg="#172033")
            card.grid(row=i // 2, column=i % 2, padx=8, pady=8, sticky="nsew")
            grid.grid_columnconfigure(i % 2, weight=1)
            grid.grid_rowconfigure(i // 2, weight=1)
            tk.Label(card, text=label, bg="#172033", fg="white",
                     font=("Segoe UI", 14, "bold")).pack(pady=(30, 10))
            tk.Label(card, text="Matplotlib visualization", bg="#172033",
                     fg="#7185a5").pack(pady=5)
            tk.Button(card, text="Open Report",
                      command=lambda f=func: self.open_chart(f),
                      bg="#6c63ff", fg="white", relief="flat",
                      padx=16, pady=8).pack(pady=18)

    def open_chart(self, func):
        try:
            func(self.manager.get_all_movies(), show=True)
        except (OSError, RuntimeError, ValueError) as exc:
            messagebox.showerror("Report Error", str(exc), parent=self)
