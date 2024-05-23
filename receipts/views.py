from django.shortcuts import render
from receipts.models import Receipt
# Create your views here.
def home(request):
    receipts = Receipt.objects.all()
    context={
        "receipts": receipts
    }
    return render(request, "receipts/home.html", context)
