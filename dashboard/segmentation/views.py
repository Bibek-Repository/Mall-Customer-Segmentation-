from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer
from .ml_model import predict_cluster
from .visualization import generate_cluster_plot

import pandas as pd


def dashboard(request):

    form = CustomerForm()

    if request.method == "POST":

        form = CustomerForm(request.POST)

        if form.is_valid():

            customer = form.save(commit=False)

            cluster = predict_cluster(
                customer.age,
                customer.annual_income,
                customer.spending_score
            )

            customer.cluster = cluster
            customer.save()

    customers = Customer.objects.all()

    data = pd.DataFrame(list(customers.values()))

    plot_path = None

    if len(data) > 0:

        plot_path = generate_cluster_plot(data)

    return render(request, "dashboard.html", {
        "form": form,
        "customers": customers,
        "plot_path": plot_path
    })
