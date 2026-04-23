import matplotlib.pyplot as plt
from collections import Counter

def plot_entity_frequency(entities):
    countries = entities.get("GPE", [])

    if not countries:
        print("No country data found.")
        return

    freq = Counter(countries)
    top = freq.most_common(5)

    names = [i[0] for i in top]
    values = [i[1] for i in top]

    plt.figure(figsize=(10, 6), facecolor="#0F172A")  # dark background
    ax = plt.gca()
    ax.set_facecolor("#0F172A")

    colors = ["#38BDF8", "#22C55E", "#F59E0B", "#A78BFA", "#F43F5E"]

    bars = plt.bar(names, values, color=colors, edgecolor="white")

    plt.title("Top Countries in Trade Policy Report",
              fontsize=16, color="white", weight="bold")
    plt.xlabel("Country", fontsize=12, color="white")
    plt.ylabel("Mentions", fontsize=12, color="white")

    plt.xticks(color="white", rotation=25)
    plt.yticks(color="white")

    # remove top/right borders
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

    # subtle grid
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    # value labels
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2,
                 yval + 0.2,
                 int(yval),
                 ha='center',
                 color='white',
                 fontsize=11)

    plt.tight_layout()

    # save high-quality image
    plt.savefig("output/chart.png", dpi=300, facecolor="#0F172A")

    plt.show()