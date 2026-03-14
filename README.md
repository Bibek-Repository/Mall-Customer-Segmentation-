# Customer Segmentation Project with Django Dashboard

## 🚀 Project Overview

This project performs **customer segmentation** using **machine learning** and provides a **web-based dashboard** to manage and visualize customer data. It combines **data analytics**, **business insights**, and a **Django web application**, making it a complete solution for businesses to understand customer behavior.

The system allows users to:

- Input new customer data through the dashboard  
- Store customer data in a database  
- Predict **customer segments** using a pre-trained **K-Means model**  
- Display an **interactive cluster visualization** highlighting the latest customer  
- Analyze customer clusters for business decisions

---

## 📂 Project Structure
customer_segmentation_project/
│
├── data/
│ ├── raw/customers.csv # Original dataset
│ └── processed/ # Cleaned & processed dataset
│
├── models/
│ └── kmeans_model.pkl # Pre-trained ML model
│
├── src/
│ ├── data_preprocessing.py # Data cleaning & scaling
│ ├── segmentation_model.py # K-Means clustering & model functions
│ ├── visualization.py # Cluster plotting with latest customer
│ └── utils.py # Folder creation & helper functions
│
├── segmentation/ # Django app
│ ├── static/segmentation/ # Static files (cluster plot)
│ ├── templates/dashboard.html # Dashboard template
│ ├── forms.py # Django form for customer input
│ ├── views.py # Dashboard views
│ ├── models.py # Customer model
│ └── ml_model.py # Load ML model & predict cluster
│
├── dashboard/ # Django project folder
│ ├── settings.py # Django settings
│ └── urls.py # URL routing
│
├── notebooks/ # Optional Jupyter notebooks
│ └── customer_segmentation_analysis.ipynb
│
├── main.py # Run entire ML pipeline standalone
├── requirements.txt # Python dependencies
└── README.md # Project documentation

customer_segmentation_project/
│
├── data/
│ ├── raw/customers.csv # Original dataset
│ └── processed/ # Cleaned & processed dataset
│
├── models/
│ └── kmeans_model.pkl # Pre-trained ML model
│
├── src/
│ ├── data_preprocessing.py # Data cleaning & scaling
│ ├── segmentation_model.py # K-Means clustering & model functions
│ ├── visualization.py # Cluster plotting with latest customer
│ └── utils.py # Folder creation & helper functions
│
├── segmentation/ # Django app
│ ├── static/segmentation/ # Static files (cluster plot)
│ ├── templates/dashboard.html # Dashboard template
│ ├── forms.py # Django form for customer input
│ ├── views.py # Dashboard views
│ ├── models.py # Customer model
│ └── ml_model.py # Load ML model & predict cluster
│
├── dashboard/ # Django project folder
│ ├── settings.py # Django settings
│ └── urls.py # URL routing
│
├── notebooks/ # Optional Jupyter notebooks
│ └── customer_segmentation_analysis.ipynb
│
├── main.py # Run entire ML pipeline standalone
├── requirements.txt # Python dependencies
└── README.md # Project documentation

ML Pipeline:

Load raw customer data

Clean missing values

Scale features (Age, Income, Spending Score)

Train K-Means clustering model

Save model for predictions

🎯 Business Insights

Using this dashboard, businesses can:

Identify high-value customers (high income + high spending)

Target underperforming segments with promotions

Visualize trends in customer spending and income

Make data-driven marketing and sales decisions

📈 Future Improvements

Interactive charts using Plotly / Bokeh

Automatic retraining of K-Means when new data is added

Export reports in PDF/Excel format

Real-time analytics dashboard with filters and hover info

Integration with live sales database

📄 References

Mall Customer Segmentation Dataset - Kaggle

Django Documentation

Scikit-Learn K-Means Clustering

Matplotlib Scatter Plots

👨‍💻 Author

Bibek Baiju – BSc IT | AI & Data Analytics Enthusiast | Web & ML Developer

LinkedIn: 

GitHub: 

Email: bibekbaiju18@gmail.com