from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context={
        "receipts": receipts
    }
    return render(request, "receipts/home.html", context)
