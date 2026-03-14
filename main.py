from src.data_preprocessing import load_data, clean_data, select_features, scale_features
from src.segmentation_model import train_kmeans, predict_clusters, save_model
from src.visualization import plot_clusters
from src.utils import create_folders

import pandas as pd

def main():

    create_folders()

    data = load_data("data/raw/customers.csv")

    data = clean_data(data)

    X = select_features(data)

    X_scaled, scaler = scale_features(X)

    model = train_kmeans(X_scaled, clusters=5)

    labels = predict_clusters(model, X_scaled)

    data['Cluster'] = labels

    data.to_csv("data/processed/segmented_customers.csv", index=False)

    save_model(model, "models/kmeans_model.pkl")

    plot_clusters(data)


if __name__ == "__main__":
    main()