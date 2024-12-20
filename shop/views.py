from django.shortcuts import render
from .models import Item

# Create your views here.
def item_view(request):
    item=Item.objects.all()
    return render(request, template_name='item_view.html', context={'item':item})