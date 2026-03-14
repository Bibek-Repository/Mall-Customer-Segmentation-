from sklearn.cluster import KMeans
import joblib

def train_kmeans(X, clusters=5):

    model = KMeans(n_clusters=clusters, random_state=42)
    model.fit(X)

    return model


def predict_clusters(model, X):

    labels = model.predict(X)

    return labels


def save_model(model, path):

    joblib.dump(model, path)