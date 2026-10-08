import tkinter as tk
from modules.analytics import MovieAnalytics
from modules.recommendations import get_preference_tags, get_recommendations

class PreferencesView(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent, bg="#0f1725")
        self.manager = manager
        self.build()

    def build(self):
        df = self.manager.get_all_movies()
        a = MovieAnalytics(df)
        tk.Label(self, text="❤️ My Movie Preferences", bg="#0f1725", fg="white",
                 font=("Segoe UI", 25, "bold")).pack(anchor="w", padx=28, pady=(26, 5))
        tk.Label(self, text="A simple profile generated from your collection.",
                 bg="#0f1725", fg="#7185a5", font=("Segoe UI", 10)).pack(anchor="w", padx=28, pady=(0, 20))

        cards = tk.Frame(self, bg="#0f1725")
        cards.pack(fill="x", padx=28)
        info = [
            ("Preferred Genre", a.preferred_genre()),
            ("Preferred Language", a.preferred_language()),
            ("Average Rating", f"{a.average_rating()}/5"),
            ("Watched", f"{a.watched_percentage()}%"),
            ("Most Active Year", str(a.yearly_summary().idxmax()) if not a.yearly_summary().empty else "N/A"),
        ]
        for title, value in info:
            f = tk.Frame(cards, bg="#172033")
            f.pack(fill="x", pady=5)
            tk.Label(f, text=title, bg="#172033", fg="#8296b5",
                     font=("Segoe UI", 9, "bold"), width=22, anchor="w").pack(side="left", padx=15, pady=12)
            tk.Label(f, text=value, bg="#172033", fg="white",
                     font=("Segoe UI", 12, "bold")).pack(side="left")

        tk.Label(self, text="Your Pattern", bg="#0f1725", fg="white",
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=28, pady=(25, 8))
        tk.Label(self, text=a.preference_summary(), bg="#0f1725", fg="#aebbd0",
                 wraplength=800, justify="left", font=("Segoe UI", 10)).pack(anchor="w", padx=28)

        tk.Label(self, text="Top Genres", bg="#0f1725", fg="white",
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=28, pady=(25, 8))
        tk.Label(self, text="  •  " + "\n  •  ".join(get_preference_tags(df)) if not df.empty else "No data",
                 bg="#0f1725", fg="#aebbd0", justify="left",
                 font=("Segoe UI", 10)).pack(anchor="w", padx=28)

        tk.Label(self, text="Suggestions From Your Collection", bg="#0f1725", fg="white",
                 font=("Segoe UI", 16, "bold")).pack(anchor="w", padx=28, pady=(25, 8))
        recs = get_recommendations(df)
        tk.Label(self, text="  •  " + "\n  •  ".join(recs) if recs else "Add more movies to generate suggestions.",
                 bg="#0f1725", fg="#aebbd0", justify="left",
                 font=("Segoe UI", 10)).pack(anchor="w", padx=28)
