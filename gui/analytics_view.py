import tkinter as tk
from tkinter import ttk

from modules.analytics import MovieAnalytics

class AnalyticsView(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent, bg="#0f1725")
        self.manager = manager
        self.build()

    def build(self):
        analytics = MovieAnalytics(self.manager.get_all_movies())
        tk.Label(self, text="Analytics", bg="#0f1725", fg="white",
                 font=("Segoe UI", 25, "bold")).pack(anchor="w", padx=28, pady=(26, 5))
        tk.Label(self, text="Understand your collection and viewing behavior.",
                 bg="#0f1725", fg="#7185a5", font=("Segoe UI", 10)).pack(anchor="w", padx=28, pady=(0, 20))

        table = ttk.Treeview(self, columns=("metric", "value"), show="headings", height=9)
        table.heading("metric", text="Metric")
        table.heading("value", text="Value")
        table.column("metric", width=280)
        table.column("value", width=280)
        metrics = [
            ("Total Movies", analytics.total_movies()),
            ("Watched Movies", analytics.watched_count()),
            ("Currently Watching", analytics.watching_count()),
            ("Plan to Watch", analytics.plan_count()),
            ("Average Rating", f"{analytics.average_rating()}/5"),
            ("Highest Rating", analytics.highest_rating()),
            ("Lowest Rating", analytics.lowest_rating()),
            ("Favorites", analytics.favorite_count()),
            ("Preferred Genre", analytics.preferred_genre()),
        ]
        for metric, value in metrics:
            table.insert("", "end", values=(metric, value))
        table.pack(anchor="w", padx=28)

        tk.Label(self, text="Average Rating by Genre", bg="#0f1725", fg="white",
                 font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=28, pady=(25, 10))
        by_genre = analytics.average_rating_by_genre()
        for genre, rating in by_genre.items():
            tk.Label(self, text=f"{genre:<18} {rating:.2f} ★",
                     bg="#0f1725", fg="#aebbd0", font=("Consolas", 10)).pack(anchor="w", padx=40, pady=2)
