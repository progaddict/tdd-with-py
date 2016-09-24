from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    model = {
        'new_item_text': request.POST.get('item_text', '')
    }
    return render(request, 'home.html', model)
