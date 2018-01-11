from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import List

def index(request):
    
    lists = List.objects.all()[:10]

    context = {
        'lists':lists
    }
    return render(request, 'index.html', context)

def details(request, id):
    list = List.objects.get(id=id)

    context = {
        'list':list
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        list = List(title=title, text=text)
        list.save()

        return redirect('/lists')
    else:
        return render(request, 'add.html')
