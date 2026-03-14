from django.db import models

class Customer(models.Model):

    age = models.IntegerField()
    annual_income = models.FloatField()
    spending_score = models.FloatField()

    cluster = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Customer {self.id}"