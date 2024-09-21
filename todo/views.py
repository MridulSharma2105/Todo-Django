from django.shortcuts import render, redirect
from django.contrib import messages

# import todo form and models

from .forms import TodoForms
from .models import Todo

# Create your views here.

def index(request):
    item_list = Todo.objects.order_by("-date")
    if (request.method == 'POST'):
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForms()
    
    page = {
        "forms" : form,
        "list" : item_list,
        "title" : "TODO List"
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')