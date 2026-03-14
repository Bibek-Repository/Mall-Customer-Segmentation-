import matplotlib.pyplot as plt

def plot_clusters(data):

    plt.figure(figsize=(8,6))

    plt.scatter(
        data['Annual Income (k$)'],
        data['Spending Score (1-100)'],
        c=data['Cluster']
    )

    plt.xlabel("Annual Income")
    plt.ylabel("Spending Score")
    plt.title("Customer Segments")

    plt.savefig("reports/figures/customer_segments.png")

    plt.show()