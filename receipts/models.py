from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="categories",
        on_delete=models.CASCADE,
    )

class Account(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="accounts",
        on_delete=models.CASCADE,
    )

class Receipt(models.Model):
    vendor = models.CharField(max_length=200)
    total = models.DecimalField(decimal_places = 3, max_digits = 10)
    tax = models.DecimalField(decimal_places = 3, max_digits = 10)
    date = models.DateTimeField(default=timezone.now)
    purchaser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="receipts",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        "ExpenseCategory",
        related_name="receipts",
        on_delete=models.CASCADE,
    )
    account = models.ForeignKey(
        "Account",
        related_name="receipts",
        on_delete=models.CASCADE,
        null=True,
    )
