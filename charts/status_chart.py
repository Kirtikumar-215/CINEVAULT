import matplotlib.pyplot as plt
from modules.analytics import MovieAnalytics

def status_chart(df, show=True):
    values = MovieAnalytics(df).status_summary()
    fig, ax = plt.subplots(figsize=(7, 5))
    if values.empty:
        ax.text(0.5, 0.5, "No data", ha="center", va="center")
    else:
        ax.pie(values.values, labels=values.index, autopct="%1.1f%%")
        ax.set_title("Viewing Status Distribution")
    fig.tight_layout()
    if show:
        plt.show()
    return fig
