import tkinter as tk
from tkinter import ttk

def make_card(parent, title, value, subtitle="", width=180):
    frame = tk.Frame(parent, bg="#172033", highlightthickness=1, highlightbackground="#26344d")
    frame.configure(width=width, height=105)
    frame.pack_propagate(False)
    tk.Label(frame, text=title, bg="#172033", fg="#91a4c3",
             font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=15, pady=(12, 0))
    tk.Label(frame, text=value, bg="#172033", fg="#ffffff",
             font=("Segoe UI", 22, "bold")).pack(anchor="w", padx=15, pady=(3, 0))
    if subtitle:
        tk.Label(frame, text=subtitle, bg="#172033", fg="#7084a5",
                 font=("Segoe UI", 8)).pack(anchor="w", padx=15)
    return frame

def style_tree(tree):
    style = ttk.Style()
    style.configure("Treeview", rowheight=32, font=("Segoe UI", 9))
    style.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))
    tree.tag_configure("favorite", background="#fff6e6")
