import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path):
    data = pd.read_csv(path)
    return data

def clean_data(data):
    data = data.dropna()
    return data

def select_features(data):
    X = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
    return X

def scale_features(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler