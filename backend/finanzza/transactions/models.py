from django.db import models
from django.contrib.auth.models import User


# Transaction Model
class Transaction(models.Model):
    INCOME = 'inc'
    EXPENSE = 'exp'
    CATEGORY_CHOICES = (
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    )

    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(
        max_length=3, choices=CATEGORY_CHOICES, default=INCOME)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_activated = models.BooleanField(default=True)
    user = models.ForeignKey(
        User, related_name='transactions', on_delete=models.CASCADE)

    def __str__(self):
        return self.description
