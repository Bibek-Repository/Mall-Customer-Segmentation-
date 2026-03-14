import os

def create_folders():

    folders = [
        "data/processed",
        "models",
        "reports/figures"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)