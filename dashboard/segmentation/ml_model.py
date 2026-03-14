import joblib
import numpy as np

model = joblib.load("../models/kmeans_model.pkl")

def predict_cluster(age, income, spending):

    data = np.array([[age, income, spending]])

    cluster = model.predict(data)

    return int(cluster[0])