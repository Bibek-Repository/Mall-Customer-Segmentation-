import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd


def generate_cluster_plot(data):

    plt.figure(figsize=(8,6))

    clusters = data['cluster'].unique()

    for c in clusters:

        subset = data[data['cluster'] == c]

        plt.scatter(
            subset['annual_income'],
            subset['spending_score'],
            label=f"Cluster {c}"
        )

    # highlight latest customer
    latest = data.iloc[-1]

    plt.scatter(
        latest['annual_income'],
        latest['spending_score'],
        marker="X",
        s=200
    )

    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segmentation")

    plt.legend()

    path = "segmentation/static/cluster_plot.png"

    plt.savefig(path)

    plt.close()

    return path