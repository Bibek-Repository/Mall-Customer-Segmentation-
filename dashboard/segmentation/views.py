from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer
from .ml_model import predict_cluster

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

    return render(request, "dashboard.html", {
        "form": form,
        "customers": customers
    })
