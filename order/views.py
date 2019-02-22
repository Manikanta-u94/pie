from django.shortcuts import render
from .models import cb,mb

# Create your views here.
def home(request):
	cb_count = cb.objects.all()
	cb_sales = len(cb_count)

	mb_count = mb.objects.all()
	mb_sales = len(mb_count)

	return render(request,'home.html',{'cb_sales':cb_sales,'mb_sales':mb_sales})
